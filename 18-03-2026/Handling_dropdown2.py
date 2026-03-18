from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')

country_dropdown= driver.find_element(By.ID, 'country')
dropdown = Select(country_dropdown)
dropdown.select_by_value('australia')
sleep(2)
dropdown.select_by_value('usa')
sleep(2)
dropdown.select_by_value('india')
sleep(2)
dropdown.select_by_index(4)
sleep(2)
dropdown.select_by_visible_text('Japan')
driver.quit()