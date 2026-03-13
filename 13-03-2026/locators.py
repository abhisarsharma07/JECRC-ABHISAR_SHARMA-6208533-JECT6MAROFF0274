from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
## ATLAS MODE
opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--headless')
driver = webdriver.Chrome(options= opts)
# sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(1)
print('Its working fine')
name = driver.find_element(By.ID, 'name')
print(name)
print('name textfield found')
phone_no=driver.find_element(By.ID, 'phone')
print(phone_no)
print("phone number found")
nav_bar = driver.find_element(By.NAME, 'Navbar')
print(nav_bar)
print('navbar found')

# radio_button = driver.find_element(By.CLASS_NAME, 'form-check-input')

# radio_button = driver.find_element(By.CLASS_NAME, 'foreck-input')
# radio_button = driver.find_element(By.CLASS_NAME,'form-check-label')
# radio_button = driver.find_elements(By.CLASS_NAME,'form-check-label')
# print(radio_button)
# print('radio button found')
# print(len(radio_button))


inp =  driver.find_elements(By.TAG_NAME, 'input')
print(len(inp))

driver.quit()
