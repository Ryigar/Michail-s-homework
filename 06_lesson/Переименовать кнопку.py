from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/textinput')

txt = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
txt.send_keys('SkyPro')
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(text)
driver.quit()