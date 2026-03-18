from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()

checkbox=driver.find_element(By.LINK_TEXT, "Checkboxes")
print("Here are the checkboxes")

sleep(2)

drag_drop=driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")
print("found")

sleep(2)

list_item=driver.find_elements(By.TAG_NAME, "li")
print("found")
print(len(list_item))

sleep(2)

driver.get("https://the-internet.herokuapp.com/tables")
sleep(2)

td= driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[2]")
print(td.text)

sleep(2)
#delete
a= driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='Bach']/following-sibling::td/a[text()='delete']")
sleep(2)

table=driver.find_element(By.XPATH, "//table[2]")
print("found")
sleep(2)

cell = driver.find_element(By.XPATH, "//table[@id='table2']//td[text()='$100.00']")
parent_tr = cell.find_element(By.XPATH, "./parent::tr")
print( parent_tr.text)
sleep(2)

driver.quit()


