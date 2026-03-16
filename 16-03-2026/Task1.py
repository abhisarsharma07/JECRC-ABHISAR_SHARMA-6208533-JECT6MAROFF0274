from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
#1
driver.get("https://opensource-demo.orangehrmlive.com/")

sleep(2)

#2

print("Page Title:",driver.title)

#3
username= driver.find_element(By.NAME, 'username')
username.clear()

#4
# username.send_keys("Abhisar")
username.send_keys("Admin")



#5
password = driver.find_element(By.NAME, "password")
# password.send_keys("Abhisar1234")
password.send_keys("admin123")

#6
login = driver.find_element(By.XPATH, "//button[@type='submit']")
login.click()
sleep(2)
#7
url = driver.current_url
print("Current URL:", url)
#8 & 9
if "dashboard" in url:
    print("Successful Login")



sleep(2)
driver.quit()