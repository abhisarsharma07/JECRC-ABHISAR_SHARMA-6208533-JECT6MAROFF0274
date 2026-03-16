from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
sleep(2)

driver.get('https://testautomationpractice.blogspot.com/')
li=['male','female']
for i in range(5):
    for j in li:
      driver.find_element(By.ID,j).click()
      sleep(2)

driver.quit()