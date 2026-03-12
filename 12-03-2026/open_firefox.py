from selenium import webdriver
opts = webdriver.FirefoxOptions()
opts.set_preference('detach', True) ## It ensures it will not go sleep
driver = webdriver.Firefox(options=opts)

driver.get('https://supertails.com')
driver.maximize_window()

# driver.close()  # it will remove the window only
driver.quit() ## it will remove complete firefox

