from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
# driver.find_element(By.LINK_TEXT,"Udemy Courses")
# print('i found the udemy link text')
# driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy Courses")
# print('i found the udemy  partial link text')


# //td[text()="Learn Java"]/following-sibling::td[3]
# //td[text()="Amod"]/ancestor::tbody/descendant::tr[2]/td[3]

xpath3=driver.find_elements(By.XPATH,'//td[text()="300"]/ancestor::tr/td[1]')
print(xpath3)
print(len(xpath3))

xpath4=driver.find_elements(By.XPATH,'//div[@class="widget-content"]/descendant::table[@id="taskTable"]/descendant::tbody/descendant::tr/td[1]')
print(xpath4)
print(len(xpath4))