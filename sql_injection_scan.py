from email import header
import requests
import re

url = input("digite sua url: ")
padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=[\w_-]+)', url)
injetion = padrao.groups()[0] + '\''

print (injetion)

header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0)'' Gecko/20100101 Firefox/103.0'}

req = requests.get(injetion, headers=header)
html = req.text

if 'mysql_fetch_array()' in html:
    print ('Vulneravel')
else:
    print('Nao vulneravel')    