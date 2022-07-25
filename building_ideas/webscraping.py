import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.get("http://www5.sefaz.mt.gov.br/")
time.sleep(2)

dado = driver.find_elements(By.NAME,"CEP")

for d in dado:
    print(d.text)

time.sleep(2)
driver.close()
