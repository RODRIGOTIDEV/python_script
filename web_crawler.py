from email import header
from socket import htonl
import requests
import re

to_crawl = [input('digite a url: ')]
crawled = set()

header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0)'' Gecko/20100101 Firefox/103.0'}

while True:

    url = to_crawl[0]

    try:
        req = requests.get(url, headers=header)
    except:
        to_crawl.remove(url)
        crawled.add(url)
        continue

    html = req.text

    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
    print('Crawling:' , url)

    to_crawl.remove(url)
    crawled.add(url)
    
    for link in links :
        if link not in crawled and link not in to_crawl:
            to_crawl.append(link)
        