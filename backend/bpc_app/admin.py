from django.contrib import admin
from .models import BPCRegistro

@admin.register(BPCRegistro)
class BPCAdmin(admin.ModelAdmin):
    list_display = ('uf', 'municipio', 'mes_competencia', 'quantidade_beneficiarios', 'valor_pago')
    list_filter = ('uf', 'mes_competencia')
