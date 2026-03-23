## Used for performing mouse and keyboard options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# action=ActionChains(driver)
# Drag And Drop
# origin_ele = driver.find_element(By.ID,'column-a')
# target_ele = driver.find_element(By.ID,'column-b')
#
# action.drag_and_drop(origin_ele,target_ele).perform()
# ## Mandatory to use .perform()
#
# sleep(2)
#
# driver.quit()

## Mouse Hover
driver.get('https://www.supertails.com/')
driver.maximize_window()

actions = ActionChains(driver)
dogesh_bhai=driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])[1]')
actions.move_to_element(dogesh_bhai).perform()
sleep(4)
driver.quit()
