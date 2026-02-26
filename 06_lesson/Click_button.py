from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get('http://uitestingplayground.com/ajax')
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
text = driver.find_element(By.CSS_SELECTOR, '.bg-success').text
print(text)
driver.quit()
