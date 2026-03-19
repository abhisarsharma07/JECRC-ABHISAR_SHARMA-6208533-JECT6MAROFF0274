from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## explicit -> for particular element and it will give timeout error always. , it is local
opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://abc.com/')
# driver.maximize_window()
# driver.implicitly_wait(5)
#
# ele= driver.find_element(By.XPATH, '(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
# print(ele.get_attribute('src'))


wait_obj= WebDriverWait(driver, 10,poll_frequency=200)
# submit_button = wait_obj.until(EC.element_to_be_clickable((By.ID,'button')))
submit_button = wait_obj.until(EC.invisibility_of_element_located((By.ID,'button')))

submit_button.click()

sleep(2)
driver.quit()
## Implicit wait
# An implicit wait in Selenium is a global setting that
# tells the WebDriver to wait for a certain amount of
# time before throwing a NoSuchElementException if an
# element is not found right away. Once you set it,
# it applies to all `findElement` and `findElements`
# calls throughout the entire session. The driver keeps
# checking the DOM repeatedly until the element appears
# or the time runs out, and if the element is found earlier,
# it continues immediately, making it better than a fixed delay
# like `sleep`. By default, the wait time is zero, so errors
# are thrown instantly. Implicit wait only checks if an element
# exists in the DOM, not whether it is visible or clickable.
# It is useful for simple and stable pages, but for dynamic
# websites where elements load at different times, explicit
# waits are usually better because they allow waiting for
# specific conditions. Also, it’s best not to use implicit
# and explicit waits together, as this can cause unpredictable delays.


## Explicit wait
# An explicit wait in Selenium is used to wait for a specific
# condition to happen before moving forward in the script.
# Unlike implicit wait, it is not global and is applied only
# to particular elements or situations where you need it.
# With explicit wait, you can wait for things like an element
# becoming visible, clickable, or having certain text.
# It works by checking the condition repeatedly until it
# is met or the maximum time is reached, and if the
# condition is satisfied earlier, the script continues
# immediately. This makes it very useful for dynamic web
# pages where elements load at different times.
# Explicit waits give more control and are more reliable
# than implicit waits, especially for complex applications,
# and they are generally preferred in most real-world automation scenarios.

# | Feature              | Implicit Wait                                                     | Explicit Wait                                                                                                                                                                    |
# | -------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | Definition           | Waits for a fixed time before throwing error if element not found | Waits for a specific condition before proceeding                                                                                                                                 |
# | Scope                | Global (applies to all elements)                                  | Local (used only where needed)                                                                                                                                                   |
# | Conditions           | Only checks if element is present in DOM                          | Checks visibility, clickability, text, etc.                                                                                                                                      |
# | Flexibility          | Less flexible                                                     | More flexible and powerful                                                                                                                                                       |
# | Best For             | Simple pages                                                      | Dynamic pages                                                                                                                                                                    |
# | **Imports (Python)** | *(no extra import needed)*                                        | `from selenium.webdriver.common.by import By`<br>`from selenium.webdriver.support.ui import WebDriverWait`<br>`from selenium.webdriver.support import expected_conditions as EC` |
# | **Example (Python)** | `driver.implicitly_wait(10)`                                      | `wait = WebDriverWait(driver, 10)`<br>`wait.until(EC.visibility_of_element_located((By.ID, "example")))`                                                                         |

#  Polling Frequency kya hota hai?
#
#  Simple words me:
#
# “Selenium kitni der ke gap me baar-baar check kare ki condition satisfy hui ya nahi”
#
# Default Behavior
#
#  By default:
#
# Polling Frequency = 0.5 seconds (500 ms)
#
# Matlab:
#
# Agar tumne WebDriverWait(driver, 10) diya
#
# To Selenium:
#  Har 0.5 sec me check karega
# Max 10 sec tak


############Fluent Wait
#
# Fluent Wait = Explicit Wait + custom polling + exception handling
#
# Matlab:
#
# Kitna wait karna hai ️
#
# Kitni interval me check karna hai
#
# Kaunse errors ignore karne hain
#
#  sab tum control kar sakte ho