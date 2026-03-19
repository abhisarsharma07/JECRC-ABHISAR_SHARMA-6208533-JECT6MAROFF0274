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


driver.get('https://www.amazon.in/')

intezaar=WebDriverWait(driver,10)
search_bar=intezaar.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="twotabsearchtextbox"]')))
search_bar.send_keys('mobiles')

fourth=intezaar.until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label="mobiles under 20000 5g phones latest"]')))
fourth.click()

sort_by= intezaar.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sort by:"]')))
sort_by.click()

new=intezaar.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Newest")]')))
new.click()


shipping = intezaar.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='p_n_free_shipping_eligible/205563695031']/span/a/div")))
shipping.click()

product = intezaar.until(EC.presence_of_element_located((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]")))

name = product.find_element(By.XPATH, '//div[@class="a-section a-spacing-small a-spacing-top-small"]/descendant::span')
price =product.find_element(By.XPATH, "//span[@class='a-price-whole']")

print(name.text," ->",price.text)
sleep(2)
driver.quit()