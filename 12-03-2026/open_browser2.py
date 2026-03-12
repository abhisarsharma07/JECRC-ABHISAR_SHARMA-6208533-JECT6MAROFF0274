from selenium import webdriver
driver = webdriver.Chrome()
# print(driver.current_url)
driver.get('https://supertails.com')
print(driver.current_url)
print(driver.title)
print(driver.name)