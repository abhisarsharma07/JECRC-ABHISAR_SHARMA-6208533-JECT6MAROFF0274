from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get(r'C:\Users\abhis\OneDrive\Desktop\Selenium\JECRC\23-03-2026\index1.html')
driver.maximize_window()
action=ActionChains(driver)

driver.find_element(By.ID, 'password').send_keys('nik')
sleep(3)
show_pwd = driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show_pwd).perform()
sleep(7)
action.release().perform()
sleep(3)
driver.quit()