import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """Открывает главную страницу магазина SauceDemo."""
        self.driver.get("https://saucedemo.com")

    @allure.step("Выполнить вход под пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """Вводит логин и пароль, нажимает кнопку Login."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Добавить товары в корзину")
    def add_products(self) -> None:
        """Добавляет рюкзак, футболку и комбинезон."""
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID,
                                 "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Заполнить форму оформления заказа")
    def fill_form(self, f_name: str, l_name: str, zip_c: str) -> None:
        """Заполняет данные пользователя и нажимает Continue."""
        self.driver.find_element(By.ID, "first-name").send_keys(f_name)
        self.driver.find_element(By.ID, "last-name").send_keys(l_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_c)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую цену")
    def get_total(self) -> str:
        return self.driver.find_element(By.CLASS_NAME,
                                        "summary_total_label").text
