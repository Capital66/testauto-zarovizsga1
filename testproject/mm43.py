from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# weblap megkeresése
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")
time.sleep(3)

# tesztadatok
email_value = ('teszt@elek.hu', 'teszt@')

# TC01 helyes kitöltés ellenőrzése
email = driver.find_element_by_id('email')
email.send_keys(email_value[0])
submit_now_button = driver.find_element_by_id('submit')
submit_now_button.click()
time.sleep(3)
val_error = driver.find_element_by_class_name('validation-error')
assert val_error.text.is_displayed() == False

# TC02 kitöltés helytelen adattal
email.clear()
email.send_keys(email_value[1])
submit_now_button.click()
time.sleep(2)
assert val_error.text == "Please enter a part following '@'. 'teszt@' is incomplete." #AssertionError - felületen magyar szöveg jelenik meg

# TC03 üres kitöltés vizsgálata
email.clear()
submit_now_button.click()
assert val_error.text == "Please fill out this field." #AssertionError - felületen magyar szöveg jelenik meg

driver.close()