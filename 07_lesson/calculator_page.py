from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(seconds)

    def click_button(self, text):
        xpath = f"//span[text()='{text}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def wait_for_result(self, value, timeout):
        WebDriverWait(self.driver, timeout + 5).until(
            EC.text_to_be_present_in_element(self.screen, value)
        )

    def get_result_text(self):
        return self.driver.find_element(*self.screen).text
