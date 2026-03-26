from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
sleep(3)

driver.find_element(By.ID, "alertButton").click()
sleep(3)
alerts = driver.switch_to.alert
alerts.accept()

driver.find_element(By.ID, "timerAlertButton").click()
sleep(8)
alert = driver.switch_to.alert
alert.accept()
sleep(3)

driver.find_element(By.ID, "confirmButton").click()
sleep(3)
alert = driver.switch_to.alert
alert.accept()

res = driver.find_element(By.ID, "confirmResult").text
assert "Ok" in res,'Cancel clicked'
print('ok')
sleep(3)

driver.find_element(By.ID, "promtButton").click()
sleep(3)
alert = driver.switch_to.alert
alert.send_keys("Selenium")
alert.accept()

result = driver.find_element(By.ID, "promptResult").text
assert "Selenium" in result, 'Not matched'
print('ok')
sleep(3)

driver.quit()