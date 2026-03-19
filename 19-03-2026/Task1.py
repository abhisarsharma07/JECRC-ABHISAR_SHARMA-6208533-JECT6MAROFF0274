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

# driver.maximize_window()
#
# for i in image:
#     print(i.get_attribute('src'))
#
# driver.quit()


driver.get('https://abc.com')
driver.maximize_window()
image = WebDriverWait(driver,10)
Waiter = image.until(EC.presence_of_all_elements_located((By.XPATH,'//figure[@class="Image aspect-ratio--parent tile__imagecontainer"]/div[2]/picture/img')))
for i in Waiter:
    print(i.get_attribute('src'))


driver.quit()