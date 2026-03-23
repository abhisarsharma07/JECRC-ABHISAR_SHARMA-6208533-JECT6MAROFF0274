from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.myntra.com/')
driver.maximize_window()
action = ActionChains(driver)
sleep(5)
wait = WebDriverWait(driver, 10)
Men= wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@data-reactid="19"]')))
action.move_to_element(Men).perform()


Jackets=wait.until(EC.visibility_of_element_located((By.XPATH,'//li[@data-reactid="40"]')))
Jackets.click()


row5=wait.until(EC.presence_of_element_located((By.XPATH,'(//ul[@class="results-base"]/li[@class="product-base"])[22]')))
action.scroll_to_element(row5).perform()
sleep(3)
driver.quit()
