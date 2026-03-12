from selenium import webdriver
from time import sleep


l1 = [webdriver.Chrome, webdriver.Edge, webdriver.Firefox]
for i in l1:
    driver = i()
    driver.get('https://github.com')
    print(driver.current_url)
    print(driver.title)
    sleep(2)

