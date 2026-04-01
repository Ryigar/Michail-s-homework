import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.screen = (By.CLASS_NAME, "screen")

    @allure.step("Открыть калькулятор")
    def open(self) -> None:
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку в {seconds} секунд")
    def set_delay(self, seconds: str) -> None:
        field = self.driver.find_element(By.ID, "delay")
        field.clear()
        field.send_keys(seconds)

    @allure.step("Нажать кнопку '{text}'")
    def click_button(self, text: str) -> None:
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    @allure.step("Ожидать появления результата '{value}'")
    def wait_for_result(self, value: str, timeout: int) -> None:
        """Ожидание текста в элементе экрана с запасом времени."""
        WebDriverWait(self.driver, timeout + 5).until(
            EC.text_to_be_present_in_element(self.screen, value)
        )

    @allure.step("Получить текущий текст с экрана")
    def get_result_text(self) -> str:
        return self.driver.find_element(*self.screen).text
