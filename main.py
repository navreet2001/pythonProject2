from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req1 = Request("https://www.indiegogo.com/individuals/23489031")
req2 = Request("https://www.indiegogo.com/individuals/4590125")
html_page = urlopen(req1, req2)


soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)