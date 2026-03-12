from selenium import webdriver
from time import sleep
## Method 1
li = ['Chrome', 'Firefox', 'Edge' ]
for i in li:
    if i =='Chrome':
        driver=webdriver.Chrome()
        sleep(2)
    elif i =='Firefox':
        driver=webdriver.Firefox()
        sleep(2)
    else:
        driver=webdriver.Edge()
        sleep(2)

#Method 2
# l1 = [webdriver.Chrome, webdriver.Edge, webdriver.Firefox]
# for i in l1:
#     driver = i()
#     sleep(2)





