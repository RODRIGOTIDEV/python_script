import requests

url = input("Digite sua url: ")

arquivo = open ('dicionario.txt')
linhas = arquivo.readlines()

for linha in True:
        
    dados = {'username': 'aaaaaa',
            'passoword': '1234'}
    resposta = requests.post(url, data=dados)    

    if "senha errados" in resposta.test:
        print("Senha incorreta")
    else:
        print ("Senha correta")