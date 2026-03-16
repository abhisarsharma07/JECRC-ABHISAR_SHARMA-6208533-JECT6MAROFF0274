# https://www.flipkart.com/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
sleep(2)
driver.get('https://www.flipkart.com/')

name=driver.find_element(By.XPATH,'//form[@class="lilxh_ header-form-search"]/descendant::div/input[@class="nw1UBF v1zwn25"]')
name.send_keys('mobiles')
print(name.get_attribute('value'))
name.send_keys(Keys.ENTER)
checkbox=driver.find_element(By.XPATH,'//label[@class="BMOCJ3 StZidb"]/input[@type="checkbox"]/following-sibling::div[text()="Apple"]')
checkbox.click()
print(checkbox.text)

abc=driver.find_element(By.XPATH,'//div[@class="fWB4Ui TTHoOY"]/img')
print(abc.get_attribute('src'))
print(abc.get_attribute('img'))
sleep(2)

driver.quit()
