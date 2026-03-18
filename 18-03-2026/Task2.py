from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
sleep(2)


a=driver.find_element(By.ID, "firstName")
a.send_keys("Monkey")
sleep(2)


b=driver.find_element(By.ID, "lastName")
b.send_keys("D. Luffy")
sleep(2)


c=driver.find_element(By.ID, "userEmail")
c.send_keys("lostZoro@gmail.com")
sleep(2)


d=driver.find_element(By.XPATH, "//label[text()='Male']")
d.click()
sleep(2)


e=driver.find_element(By.ID, "userNumber")
e.send_keys("9090808070")
sleep(2)


subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("Physics")
subject.send_keys(Keys.ENTER)
sleep(2)


f=driver.find_element(By.XPATH, "//label[text()='Reading']")
f.click()
sleep(2)


driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\abhis\Downloads\Pie_1.png")
sleep(2)


driver.find_element(By.ID, "currentAddress").send_keys("JECRC")
sleep(2)

state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("Rajasthan", Keys.ENTER)
sleep(2)


y = driver.find_element(By.ID, "react-select-4-input")
y.send_keys("Jaiselmer", Keys.ENTER)
sleep(2)


z=driver.find_element(By.ID, "submit")
z.click()
sleep(3)

driver.quit()