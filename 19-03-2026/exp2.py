from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
## explicit -> for particular element and it will give timeout error always. , it is local
opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=opts)
# driver.get('https://abc.com/')
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver, 5)
# enable_btn= wait.until(EC.element_to_be_clickable(By.ID, 'enableAfter'))

# It is a bad practice to use this upper code




