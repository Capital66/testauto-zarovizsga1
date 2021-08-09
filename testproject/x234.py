from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# weblap megkeresése
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")
time.sleep(3)

# tesztadatok
a_value = ('99', 'kiskutya')
b_value = ('12', '12')

# TC01 helyes kitöltés ellenőrzése
a = driver.find_element_by_id('a')
a.send_keys(a_value[0])
b = driver.find_element_by_id('b')
b.send_keys(b_value[0])
kalkulacio_button = driver.find_element_by_id('submit')
kalkulacio_button.click()
eredmeny = driver.find_element_by_id('result')
time.sleep(2)
assert eredmeny.text == '222'

# TC02 kitöltés nem számokkal
a.clear()
b.clear()
a.send_keys(a_value[1])
b.send_keys(b_value[1])
kalkulacio_button.click()
time.sleep(2)
assert eredmeny.text == 'NaN'

# TC03 üres kitöltés vizsgálata
a.clear()
b.clear()
kalkulacio_button.click()
time.sleep(2)
assert eredmeny.text == 'NaN'

driver.close()
