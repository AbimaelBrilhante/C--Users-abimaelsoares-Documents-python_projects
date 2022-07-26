import requests
from selenium import webdriver
driver = webdriver.Firefox()
from bs4 import BeautifulSoup


page = requests.get("http://www5.sefaz.mt.gov.br/")
soup = BeautifulSoup(page.text, 'html.parser')
endereco = soup.find

for e in endereco:
    print(e)
page.close()

