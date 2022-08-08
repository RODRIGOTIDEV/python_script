from turtle import st
import requests
import re

to_crawl = [input('digite a url: ')]
crawled = set()
emails_found = set()

header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0)'' Gecko/20100101 Firefox/103.0'}

for i in range(10):
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

    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+\w', html)

    print(emails)

    to_crawl.remove(url)
    crawled.add(url)
    
    for link in links :
        if link not in crawled and link not in to_crawl:
            to_crawl.append(link)

    for email in emails:
        emails_found.add(email)    
print ('###################################################################################')
print ('')
print ("Email: " ,emails_found)        
print ('')
print ('###################################################################################')
