from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/droppable')
#
# driver.maximize_window()
# sleep(2)
# action=ActionChains(driver)
# origin_ele = driver.find_element(By.XPATH,'//div[@id="draggable"]')
# target_ele = driver.find_element(By.XPATH,'(//div[@id="droppable"])[1]')
# action.drag_and_drop(origin_ele,target_ele).perform()
# sleep(5)
#
# assert 'Dropped' == target_ele.text, 'Not Done'
# driver.quit()


##Drag and Drop using wait

# driver = webdriver.Chrome()
# driver.get('https://demoqa.com/droppable')
driver.maximize_window()
sleep(3)
wait = WebDriverWait(driver, 10)
origin_ele = wait.until(EC.visibility_of_element_located((By.ID, 'draggable')))
target_ele = wait.until(EC.visibility_of_element_located((By.ID, 'droppable')))
actions = ActionChains(driver)
actions.drag_and_drop(origin_ele, target_ele).perform()
a = wait.until(EC.visibility_of_element_located((By.ID, 'droppable')))
assert 'Dropped!' == a.text, 'Not Done'
print('Done perfectly')
