from django.core.management.base import BaseCommand
from bpc_app.models import BPCRegistro
import csv
from datetime import datetime

class Command(BaseCommand):
    help = 'Importa dados do BPC a partir de um CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Caminho para o arquivo CSV do BPC')

    def handle(self, *args, **kwargs):
        path = kwargs['csv_path']
        with open(path, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            total = 0
            for row in reader:
                BPCRegistro.objects.create(
                    uf=row['UF'],
                    municipio=row['Município'],
                    codigo_municipio=int(row['Código IBGE Município']),
                    mes_competencia=datetime.strptime(row['Competência'], '%Y-%m'),
                    quantidade_beneficiarios=int(row['Quantidade de Beneficiários'].replace('.', '').replace(',', '')),
                    valor_pago=float(row['Valor Pago'].replace('R$', '').replace('.', '').replace(',', '.'))
                )
                total += 1
        self.stdout.write(self.style.SUCCESS(f'{total} registros importados com sucesso.'))
