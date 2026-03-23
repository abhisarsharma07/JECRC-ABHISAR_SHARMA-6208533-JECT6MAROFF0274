from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://supertails.com/')
driver.maximize_window()
sleep(5)

action= ActionChains(driver)
billi= driver.find_element(By.XPATH, '//div[@data-ganame="Breed 5"]')
action.scroll_to_element(billi).perform()
sleep(5)
action.scroll_by_amount(0,-500).perform() ## it is taking value in pixels and -500 to scroll up and +500 to scroll down
sleep(3)
# action.scroll_from_origin(billi, 0,500).perform()
# Traceback (most recent call last):
#   File "C:\Users\abhis\OneDrive\Desktop\Selenium\JECRC\23-03-2026\scroll.py", line 22, in <module>
#     action.scroll_from_origin(billi, 0,500).perform()
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\abhis\AppData\Local\Programs\Python\Python311\Lib\site-packages\selenium\webdriver\common\action_chains.py", line 362, in scroll_from_origin
#     raise TypeError(f"Expected object of type ScrollOrigin, got: {type(scroll_origin)}")
# TypeError: Expected object of type ScrollOrigin, got: <class 'selenium.webdriver.remote.webelement.WebElement'>
#

##
driver.quit()
# SCROLL TO: (0,100)
# SCROLL BY: ()

