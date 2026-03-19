from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)


driver.get('https://qavbox.github.io/demo/signup/')

pratiksha1=WebDriverWait(driver,10)
Fullname= pratiksha1.until(EC.visibility_of_element_located((By.NAME, "uname")))
Fullname.send_keys("Narendra D Modi")

email=pratiksha1.until(EC.visibility_of_element_located((By.ID, "email")))
email.send_keys("PrimeMinister@gmail.com")


telephone=pratiksha1.until(EC.visibility_of_element_located((By.ID, "tel")))
telephone.send_keys("7859756822")


file=pratiksha1.until(EC.visibility_of_element_located((By.NAME, "datafile")))
file.send_keys(r"C:\Users\abhis\OneDrive\Desktop\github-logo.png""")

dropdown= pratiksha1.until(EC.visibility_of_element_located((By.NAME, "sgender")))
ab=Select(dropdown)
ab.select_by_value('male')

six=pratiksha1.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='six']")))
six.click()

checkbox=pratiksha1.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='c#']")))
checkbox.click()

AT = pratiksha1.until(EC.visibility_of_element_located((By.ID, "tools")))
select1 = Select(AT)
select1.select_by_visible_text("CodedUI")

btn=pratiksha1.until(EC.visibility_of_element_located((By.ID, "submit")))
btn.click()
sleep(2)

driver.quit()
