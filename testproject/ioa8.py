from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# weblap megkeresése
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")
time.sleep(3)

# számok, műveleti jel kikeresése
elso_szam = driver.find_element_by_id('num1')
elso_szam_value = int(elso_szam.text)
masodik_szam = driver.find_element_by_id('num2')
masodik_szam_value = int(masodik_szam.text)
muvelet = driver.find_element_by_id('op')
muvelet_jel = muvelet.text.strip()

print(elso_szam_value)
print(muvelet_jel)
print(masodik_szam_value)

eredmeny = (elso_szam_value)(muvelet_jel)(masodik_szam_value)

# kalkuláció, ellenőrzés
kalkulacio_button = driver.find_element_by_id('submit')
kalkulacio_button.click()
eredmeny_calc = driver.find_element_by_id('result').get_attribute('value')
assert eredmeny == int(eredmeny_calc)

driver.close()
