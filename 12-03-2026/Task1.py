from selenium import webdriver
from time import sleep

## ## use all methods in one script


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.get("https://supertails.com")
sleep(2)
driver.maximize_window()
sleep(2)
driver.get("https://github.com/abhisarsharma07/JECRC-ABHISAR_SHARMA-6208533-JECT6MAROFF0274")
sleep(2)
print("Current URL:", driver.current_url)
print("Browser Name:", driver.name)
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.minimize_window()
sleep(2)
# driver.close()
driver.quit()
# driver = webdriver.Chrome()
# sleep(1)
# # sleep(5)
#
# # driver =webdriver.Firefox()
# # sleep(5)
# #pip install webdriver-manager -> to manually Install Web Browser..
#
# driver.get('https://supertails.com')
# driver.maximize_window()
# sleep(2)
# driver.maximize_window()
# sleep(2)
# # driver.maximize_window()
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True) ## It ensures it will not go sleep
# driver = webdriver.Chrome(options=opts)
# driver.get('https://github.com')
#
# print(driver.current_url)
# print(driver.title)
# print(driver.name)
