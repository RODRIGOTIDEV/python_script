import requests

url = input(u"digite sua URL: ")
dado = input("Digiti valor do dados: ")

cabecalho = {''}
parametros = {dado : '10' }

resposta = requests.get(url, headers=cabecalho)

print (resposta.text)