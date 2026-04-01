import allure
import pytest
from selenium import webdriver

from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.epic("Домашнее задание №10")
@allure.feature("Медленный калькулятор")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Сложение 7 + 8 с задержкой")
@allure.description(
    "Проверка корректности работы калькулятора при установленном delay в 45 сек.")
def test_slow_addition(browser):
    calc = CalculatorPage(browser)
    calc.open()
    calc.set_delay("45")

    with allure.step("Ввод примера: 7 + 8 ="):
        for btn in ["7", "+", "8", "="]:
            calc.click_button(btn)

    calc.wait_for_result("15", 45)

    with allure.step("Проверка итогового результата на экране"):
        assert calc.get_result_text() == "15"
