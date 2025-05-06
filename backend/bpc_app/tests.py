from rest_framework.test import APITestCase
from django.urls import reverse
from .models import BPCRegistro

class BPCRegistroAPITests(APITestCase):
    def setUp(self):
        BPCRegistro.objects.create(
            uf="SP",
            municipio="São Paulo",
            codigo_municipio=3550308,
            mes_competencia="2023-01-01",
            quantidade_beneficiarios=100,
            valor_pago=150000.00
        )

    def test_status_endpoint(self):
        response = self.client.get("/api/status/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "online"})

    def test_estados_endpoint(self):
        response = self.client.get("/api/bpc/estados/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("SP", response.json())

    def test_analise_endpoint(self):
        response = self.client.get("/api/bpc/analise/?uf=SP&periodo=2023-01-01,2023-12-31")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_discrepantes_endpoint(self):
        response = self.client.get("/api/bpc/discrepantes/")
        self.assertEqual(response.status_code, 200)

    def test_cidades_endpoint(self):
        response = self.client.get("/api/bpc/cidades/?uf=SP")
        self.assertEqual(response.status_code, 200)
        self.assertIn("São Paulo", response.json())
