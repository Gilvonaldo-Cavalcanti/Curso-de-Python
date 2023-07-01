import requests
from bs4 import BeautifulSoup as bs

#Faz a solicitação GET para o URL desejado
response = requests.get("https://pt.wikipedia.org/")

#Verifica se a solcitação foi bem-sucedida
if response.status_code == 200:
    #Cria um objeto BeautifulSoup com o conteúdo HTML da página desejada
    soup = bs(response.content, "html.parser")

    #Extração de dados
    titulo = soup.find("h1").text
    paragrafos = soup.find_all("p")

    #Imprime os dados
    print("Título:", titulo)
    print("Parágrafos:")
    for p in paragrafos:
        print("-",p.text)