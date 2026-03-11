import pytest
from selenium import webdriver

from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_addition(browser):
    calc = CalculatorPage(browser)
    calc.open()
    calc.set_delay("45")

    for btn in ["7", "+", "8", "="]:
        calc.click_button(btn)

    calc.wait_for_result("15", 45)
    assert calc.get_result_text() == "15"
