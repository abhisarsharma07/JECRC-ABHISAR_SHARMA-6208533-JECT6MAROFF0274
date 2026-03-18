from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep


opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.lenskart.com/')
ab=driver.find_element(By.XPATH, '//input[@class="aa-Input"]')
ab.send_keys('Sunglasses', Keys.ENTER)
driver.maximize_window()
sleep(5)
tx=driver.find_element(By.XPATH, '//select[@id="sortByDropdown"]')
drop=Select(tx)
drop.select_by_value('saving')
sleep(5)

gta=driver.find_element(By.XPATH,'//div[@class="sc-23b7d3eb-6 hYdmOJ"]/div/following-sibling::p')
print(gta.text)
sleep(2)
driver.quit()