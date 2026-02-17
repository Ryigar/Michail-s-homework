from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/login')
input_username = (driver.find_element(By.CSS_SELECTOR, '#username'))
input_password = (driver.find_element(By.CSS_SELECTOR, '#password'))
input_username.send_keys('tomsmith')
input_password.send_keys('SuperSecretPassword!')
driver.find_element(By.CSS_SELECTOR, '.fa-2x').click()
text = driver.find_element(By.CSS_SELECTOR, '#flash').text
print(text)
driver.quit()
