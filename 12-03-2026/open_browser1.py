from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True) ## It ensures it will not go sleep
driver = webdriver.Chrome(options=opts)

driver.get('https://supertails.com')
