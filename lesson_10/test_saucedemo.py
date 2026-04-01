import allure
import pytest
from selenium import webdriver

from pages import LoginPage, InventoryPage, CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.epic("Домашнее задание №10")
@allure.feature("Магазин SauceDemo")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Покупка набора товаров")
@allure.description(
    "Проверка сценария: логин, выбор товаров и сверка финальной цены.")
def test_buy_products(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_products()
    inventory_page.go_to_cart()

    with allure.step("Нажать кнопку Checkout в корзине"):
        driver.find_element("id", "checkout").click()

    checkout_page.fill_form("Михаил", "Мещеряков", "410008")

    with allure.step("Проверка итоговой суммы заказа"):
        total_text = checkout_page.get_total()
        assert "58.29" in total_text
