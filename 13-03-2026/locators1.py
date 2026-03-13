from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
## ATLAS MODE
opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--headless')
driver = webdriver.Chrome(options= opts)
# sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(1)

# input[class="form-control"]
# input[type="radio"]
# animals=driver.find_element(By.CSS_SELECTOR,'select[id="animals"]')
# animals=driver.find_element(By.CSS_SELECTOR,'#animals')
# a[href*="testautomationpractice"]  ## * is for partial --- it will  we can write partial name and it will find it
# a[href^="https://"] ## It will found all the html element which were starting from the https:// .... ^ is for all the start from
# a[href$=".com"] ## $ used for endswith

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
## ATLAS MODE
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
# opts.add_argument('--headless')
driver = webdriver.Chrome(options= opts)
# sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(1)
## css selector
animals = driver.find_element(By.CSS_SELECTOR,'select[id="animals"]')
animals1 = driver.find_element(By.CSS_SELECTOR,'#animals') ## for id we use (#), (.) for class name
anc = driver.find_element(By.CSS_SELECTOR,'a[href*="testautomationpractice"]') ## * used to give partial text, that is automation check that this sub string is present in whole string
anc1 = driver.find_element(By.CSS_SELECTOR,'a[href^="https://"]') ## ^ is show that my whole string start with ....
anc2 = driver.find_element(By.CSS_SELECTOR,'a[href$=".com"]') ## $ is show that my whole string ends with ....
print(animals)
# print("It worked out")
print(animals1)
print("It worked out")
print(f'It worked anc: {anc}')
print(f'It worked anc1: {anc1}')
print(f'It worked anc1: {anc2}')
driver.quit()
print("working goos")
driver.quit()

# div[class=""]
## We cant find inner content inside a tag

# input[type="text"][class="register"]
