from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
sleep(2)
driver.get('https://testautomationpractice.blogspot.com/')

li=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for k in li:
    driver.find_element(By.XPATH, f'//label[text()="{k}"]').click()
    print(driver.find_element(By.XPATH, f'//label[text()="{k}"]').text)
    sleep(2)

for i in li[::-1]:
    driver.find_element(By.XPATH, f'//label[text()="{i}"]').click()
    print(driver.find_element(By.XPATH, f'//label[text()="{i}"]').text)
    sleep(2)

driver.quit()