from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
sleep(3)
iframe = driver.find_element(By.ID, 'singleframe')
# driver.switch_to.frame(iframe)
driver.switch_to.window(iframe)
sleep(2)
driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('123')
sleep(2)


## iframe within iframe

driver.find_element(By.XPATH, '//a[text()="Iframe with in an iframe"]').click()