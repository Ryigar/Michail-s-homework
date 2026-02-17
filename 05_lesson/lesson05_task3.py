from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/inputs')
input_str = (driver.find_element(By.CSS_SELECTOR, '[type="number"]'))
input_str.send_keys('Sky')
input_str.clear()
input_str.send_keys('Pro')
driver.quit()
