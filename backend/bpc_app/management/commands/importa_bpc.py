from django.core.management.base import BaseCommand
import requests, os, zipfile
from bs4 import BeautifulSoup
from io import BytesIO
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

class Command(BaseCommand):
    help = "Faz o scraping e importa os dados BPC automaticamente"

    def handle(self, *args, **kwargs):
        BASE_URL = "https://portaldatransparencia.gov.br/download-de-dados/bpc"
        DATA_DIR = "/tmp/bpc"
        os.makedirs(DATA_DIR, exist_ok=True)

        print("🔍 Buscando link mais recente...")
        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a", href=True)
        zip_links = sorted({l["href"] for l in links if "bpc" in l["href"].lower() and l["href"].endswith(".zip")}, reverse=True)

        if not zip_links:
            raise Exception("❌ Nenhum link ZIP BPC encontrado.")

        full_url = zip_links[0]
        if not full_url.startswith("http"):
            full_url = "https://portaldatransparencia.gov.br" + full_url

        print(f"⬇️ Baixando: {full_url}")
        r = requests.get(full_url)
        z = zipfile.ZipFile(BytesIO(r.content))
        z.extractall(DATA_DIR)

        csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
        if not csv_files:
            raise Exception("❌ Nenhum arquivo CSV encontrado após extração.")
        file_path = os.path.join(DATA_DIR, csv_files[0])
        print(f"📄 Importando: {file_path}")

        df = pd.read_csv(file_path, sep=";", encoding="utf-8")
        df["UF"] = df["UF"].astype(str)
        df["Município"] = df["Município"].astype(str)
        df["Código IBGE Município"] = df["Código IBGE Município"].astype(int)
        df["Competência"] = pd.to_datetime(df["Competência"], format="%Y-%m")
        df["Quantidade de Beneficiários"] = df["Quantidade de Beneficiários"].replace({r"\D": ""}, regex=True).astype(int)
        df["Valor Pago"] = df["Valor Pago"].replace({r"[R$\s]": "", r"\.": "", r",": "."}, regex=True).astype(float)

        registros = [
            (
                row["UF"],
                row["Município"],
                row["Código IBGE Município"],
                row["Competência"],
                row["Quantidade de Beneficiários"],
                row["Valor Pago"],
            )
            for _, row in df.iterrows()
        ]

        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise Exception("❌ DATABASE_URL não está configurado.")

        print("📤 Inserindo registros no banco...")
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute("DELETE FROM bpc_app_bpcregistro")
        execute_values(
            cur,
            """
            INSERT INTO bpc_app_bpcregistro
            (uf, municipio, codigo_municipio, mes_competencia, quantidade_beneficiarios, valor_pago)
            VALUES %s
            """,
            registros
        )
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Dados importados com sucesso.")

