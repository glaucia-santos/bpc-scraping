from django.db import models

class BPCRegistro(models.Model):
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=100)
    codigo_municipio = models.IntegerField()
    mes_competencia = models.DateField()
    quantidade_beneficiarios = models.IntegerField()
    valor_pago = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.municipio} - {self.mes_competencia}"
