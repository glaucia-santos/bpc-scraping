import requests
from bs4 import BeautifulSoup

def baixar_arquivo_bpc():
    url = "https://portaldatransparencia.gov.br/download-de-dados/bpc"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        link = soup.find("a", string="BPC")['href']
        print("Link para download:", link)
    else:
        print("Erro ao acessar a página")
