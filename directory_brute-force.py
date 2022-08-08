import requests

url = "https://online.igti.com.br/"
arquivo = open('lista.txt')
linhas = arquivo.readlines()

for linha in linhas:
    if linha [0] != "#":
        diretorio = arquivo
        resposta =  requests.get(url+diretorio)
        codigo = resposta.status_code
    if codigo != 404 and codigo != 403:
        print (url+linha, codigo)