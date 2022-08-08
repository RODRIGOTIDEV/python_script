from wsgiref import headers
import urllib
import urllib3
url = input("igite sua url: ")

cabecalho = {""}

requisicao = urllib.Request(url, headers=cabecalho)
resposta = urllib3.urlopen(url,)
