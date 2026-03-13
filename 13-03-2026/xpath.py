from selenium import webdriver
from selenium.webdriver.common.by import By
# //input[@placeholder="Enter Name"]
# webdriver=webdriver.Chrome()
## ATLAS MODE
opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--headless')
driver = webdriver.Chrome(options= opts)
# sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
xpath1=driver.find_element(By.XPATH ,'//input[@placeholder="Enter Name"]')
print(xpath1)

xpath2=driver.find_element(By.XPATH ,'//label[@for="gender"]')
print(xpath2)

xpath3=driver.find_element(By.XPATH ,'//input[@value="sunday"]')
print(xpath3)

xpath4 = driver.find_element(By.XPATH ,'//link[@rel="Stylesheet"]')
print(xpath4)

xpath5= driver.find_element(By.XPATH,'//div[@class="footer-outer"]')
print(xpath5)

print("done")
xpath6=driver.find_element(By.XPATH,'//a[text()="Home"]')
xpath7=driver.find_element(By.XPATH,'//a[text()="Udemy Courses"]')
xpath8=driver.find_element(By.XPATH,'//a[text()="Online Trainings"]')
xpath9=driver.find_element(By.XPATH,'//a[text()="Blog"]')
xpath10=driver.find_element(By.XPATH,'//a[text()="PlaywrightPractice"]')
xpath11=driver.find_element(By.XPATH,'//option[contains(text()," Blue")]') # if there is an extra space ahead of anything like _Blue .. Then we will do it
print(xpath6)
print(xpath7)
print(xpath8)
print(xpath9)
print(xpath10)
print(xpath11)