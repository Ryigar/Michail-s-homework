from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
image = driver.find_element(By.CSS_SELECTOR, '#award')
print(image.get_attribute('src'))
driver.quit()
