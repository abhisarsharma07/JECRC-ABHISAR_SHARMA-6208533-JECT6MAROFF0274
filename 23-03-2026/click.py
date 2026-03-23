from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://supertails.com/')
driver.maximize_window()
action = ActionChains(driver)
sleep(5)
# action.send_keys(Keys.PAGE_DOWN).perform() ## PAGE NEECHE
# sleep(5)
# action.send_keys(Keys.PAGE_UP).perform() ##PAGE OOPER
# sleep(5)
## action.context_click()
## action.double_click()
action.key_down(Keys.CONTROL).send_keys('a').perform()  ##PRESS
sleep(2)
action.key_up(Keys.CONTROL).perform() ##RELEASE
sleep(2)
driver.quit()

