
import os
import time
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Configurações
URL = "https://portaldatransparencia.gov.br/download-de-dados/bpc"
DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def configurar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    prefs = {"download.default_directory": os.path.abspath(DOWNLOAD_DIR)}
    chrome_options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def baixar_e_extrair(driver):
    driver.get(URL)
    time.sleep(3)

    links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.zip']")
    for link in links:
        href = link.get_attribute("href")
        nome_arquivo = href.split("/")[-1]
        caminho_destino = os.path.join(DOWNLOAD_DIR, nome_arquivo)

        if not os.path.exists(caminho_destino):
            print(f"Baixando: {nome_arquivo}")
            driver.get(href)
            time.sleep(10)  # Espera o download
            if os.path.exists(caminho_destino):
                with zipfile.ZipFile(caminho_destino, 'r') as zip_ref:
                    zip_ref.extractall(DOWNLOAD_DIR)
                print(f"Extraído: {nome_arquivo}")
        else:
            print(f"Arquivo já existente: {nome_arquivo}")

if __name__ == "__main__":
    driver = configurar_driver()
    try:
        baixar_e_extrair(driver)
    finally:
        driver.quit()
