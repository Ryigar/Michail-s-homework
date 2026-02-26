from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
image = images[3]
print(image.get_attribute('src'))
driver.quit()
