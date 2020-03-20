import requests
from lxml import html
from bs4 import BeautifulSoup

url = 'https://burgerking.ru'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
print(soup.link, soup.link.name, soup.link.text)