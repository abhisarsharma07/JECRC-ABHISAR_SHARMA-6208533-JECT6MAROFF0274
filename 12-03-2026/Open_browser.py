## To Open Chrome Browser
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(1)
# sleep(5)

# driver =webdriver.Firefox()
# sleep(5)
#pip install webdriver-manager -> to manually Install Web Browser..

driver.get('https://supertails.com')
driver.maximize_window()
sleep(2)
# driver.maximize_window()
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)