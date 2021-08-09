from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# weblap megkeresése
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")
time.sleep(3)

# 100 pénzfeldobás
penzfeldobas_button = driver.find_element_by_id('submit')
for i in range(100):
    penzfeldobas_button.click()
    time.sleep(0.1)
eredmeny_numbers = driver.find_elements_by_xpath('//*[@id="results"]/li')
assert len(eredmeny_numbers) == 100

# minimum 30 fej
eredmeny_text = driver.find_elements_by_xpath('//*[@id="results"]/li/text()')
for j in eredmeny_text:
    j.count('fej')
assert j.count() >= 30

driver.close()
