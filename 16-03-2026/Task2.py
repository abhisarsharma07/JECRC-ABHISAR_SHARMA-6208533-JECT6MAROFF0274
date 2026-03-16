from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/radio-button')
print("Page Title:", driver.title)

sleep(2)

yes=driver.find_element(By.XPATH, "//input[@id='yesRadio']")
yes.click()
sleep(2)

result = driver.find_element(By.XPATH, '//p[@class="mt-3"]')
print("Rrsult message:", result.text)

print("Radio Button Class:", yes.get_attribute("class"))
print("Radio Button ID:", yes.get_attribute("for"))

print("Current URL:", driver.current_url)
sleep(2)
driver.quit()