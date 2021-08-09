from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# weblap megkeresése
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")
time.sleep(3)

# létező városok kiolvasása
select_cities = Select(driver.find_element_by_id('cites')).select_by_visible_text()
print(select_cities)
time.sleep(3)

# városok lista
cities_list = driver.find_elements_by_id('randomCities')
for i in cities_list:
    print(cities)

# a hiányzó város beírása, ellenőrzés
city = driver.find_element_by_id('missingCity')
city.send_keys()
ellenorzes_button = driver.find_element_by_id('submit')
ellenorzes_button.click()

driver.close()

