from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
sleep(2)

# driver.get("https://www.cricbuzz.com/")
# sleep(2)
#
# driver.get("https://www.myntra.com/")
# sleep(2)

xpath1=driver.find_element(By.XPATH, '//a[text()="Fresh"]/ancestor::li/following-sibling::li[1]')
print(xpath1)

