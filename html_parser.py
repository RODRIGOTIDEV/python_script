from bs4 import BeautifulSoup
import requests

url = input('digite sua url:')
header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0)'' Gecko/20100101 Firefox/103.0'}

req = requests.get(url, headers=header)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

print (soup.prettify)