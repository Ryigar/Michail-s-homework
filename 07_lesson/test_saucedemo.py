import pytest
from selenium import webdriver

from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_buy_products(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack()
    inventory_page.add_bolt_tshirt()
    inventory_page.add_onesie()

    inventory_page.go_to_cart()
    cart_page.checkout()

    checkout_page.fill_form("Михаил", "Мещеряков", "410008")
    total_text = checkout_page.get_total_price()

    assert "58.29" in total_text, f"Ожидали $58.29, получили: {total_text}"
