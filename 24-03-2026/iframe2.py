from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

action = ActionChains(driver)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(3)

#switching to frame
# frame = driver.find_element(By.ID, "singleframe")
# driver.switch_to.frame(frame)            #driver.switch_to.window()
# sleep(2)
# driver.find_element(By.XPATH,"//input[@type = 'text']").send_keys("abab")
# sleep(4)

#nested-iframe
driver.find_element(By.XPATH,"//a[text() = 'Iframe with in an Iframe']").click()
frame_out =  driver.find_element(By.XPATH, '//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(frame_out)
frame_in =  driver.find_element(By.XPATH, '//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(frame_in)


driver.find_element(By.XPATH,"//input[@type = 'text']").send_keys("abab")
sleep(3)