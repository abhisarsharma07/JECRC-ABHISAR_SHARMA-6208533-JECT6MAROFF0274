from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://accounts.shopify.com/lookup?rid=e7328d56-761d-470c-b824-f08d7cbc9aff&verify=1773644895-sXrkD5G4EFOYRKBP2DlrUa1B%2BY94SrxWXonfyMC5JrI%3D')
name=driver.find_element(By.XPATH,'//input[@class="next-input email-typo-input"]')
name.send_keys('HARSHU@gmail.com')
sleep(1)
name.clear()
# name.click()

sleep(2)
name.send_keys('Abhisar@gmail.com', Keys.ENTER)
# print(name.get_attribute('placeholder'))
print(name.get_attribute('value'))
sleep(5)
driver.maximize_window()