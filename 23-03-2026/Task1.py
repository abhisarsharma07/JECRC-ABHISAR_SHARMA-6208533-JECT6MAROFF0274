# (//img[@class="image lazyloaded"])[4]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.rajasthanroyals.com/')
driver.maximize_window()
action = ActionChains(driver)
sleep(5)
# Sanju_Samson=driver.find_element(By.XPATH, '(//div[@class="article-wrap"])[26]')
wait = WebDriverWait(driver, 10)
Sanju_Samson=wait.until(EC.presence_of_element_located((By.XPATH,'(//div[@class="article-wrap"])[26]')))
for i in range(5):
    action.scroll_to_element(Sanju_Samson).perform()
    sleep(2)
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(2)


driver.quit()