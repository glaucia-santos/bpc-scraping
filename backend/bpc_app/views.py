from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Avg
from .models import BPCRegistro
from .serializers import BPCRegistroSerializer
from rest_framework.views import APIView
from rest_framework.response import Response




class StatusView(APIView):
    def get(self, request):
        return Response({"status": "online"})


class BPCRegistroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BPCRegistro.objects.all()
    serializer_class = BPCRegistroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uf', 'municipio']

    @action(detail=False, methods=['get'])
    def analise(self, request):
        estado = request.GET.get('uf')
        cidade = request.GET.get('municipio')
        periodo = request.GET.get('periodo')

        registros = self.queryset

        if estado:
            registros = registros.filter(uf=estado)
        if cidade:
            registros = registros.filter(municipio=cidade)
        if periodo:
            inicio, fim = periodo.split(',')
            registros = registros.filter(mes_competencia__range=[inicio, fim])

        agregados = registros.values('mes_competencia').annotate(
            total_beneficiarios=Sum('quantidade_beneficiarios'),
            total_pago=Sum('valor_pago')
        ).order_by('mes_competencia')

        return Response(agregados)

    @action(detail=False, methods=['get'])
    def discrepantes(self, request):
        media_nacional = self.queryset.aggregate(media=Avg('valor_pago'))['media'] or 0
        discrepantes = self.queryset.filter(valor_pago__gt=2*media_nacional).values(
            'uf', 'municipio', 'mes_competencia', 'valor_pago', 'quantidade_beneficiarios'
        ).order_by('-valor_pago')[:50]
        return Response(discrepantes)

    @action(detail=False, methods=['get'])
    def estados(self, request):
        estados = self.queryset.values_list('uf', flat=True).distinct()
        return Response(sorted(list(estados)))

    @action(detail=False, methods=['get'])
    def cidades(self, request):
        uf = request.GET.get('uf')
        if uf:
            cidades = self.queryset.filter(uf=uf).values_list('municipio', flat=True).distinct()
            return Response(sorted(list(cidades)))
        return Response([])


