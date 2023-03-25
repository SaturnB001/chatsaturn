import googlesearch
import urllib.request
from bs4 import BeautifulSoup

print("Olá, eu sou um chatbot! O que você gostaria de saber?")

while True:
    # Recebe a pergunta do usuário
    pergunta = input("> ")

    # Usa o módulo googlesearch para buscar a resposta na web
    resultados = googlesearch.search(pergunta, num_results=3)

    # Acessa o primeiro link encontrado e extrai o texto da página
    resposta = ""
    for link in resultados:
        try:
            html = urllib.request.urlopen(link).read()
            soup = BeautifulSoup(html, 'html.parser')
            texto = soup.get_text()
            resposta += texto
            break
        except:
            pass

    # Imprime a resposta encontrada
    print(resposta)
