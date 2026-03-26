
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
driver.maximize_window()
sleep(3)
driver.switch_to.frame("result")

username = driver.find_element(By.ID, "username")
username.clear()
username.send_keys("testuser")
passwd = driver.find_element(By.ID, "password")
passwd.clear()
passwd.send_keys("testpass")

eye = driver.find_element(By.ID, "showPsswd")
actions = ActionChains(driver)
actions.click_and_hold(eye).perform()
sleep(3)
actions.release().perform()

driver.find_element(By.CLASS_NAME, "submit").click()
sleep(5)
# driver.refresh()
text = driver.find_element(By.TAG_NAME, "h1").text
assert "Registration" in text

driver.quit()