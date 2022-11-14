from selenium.webdriver.common.by import By


class BasePageLocators:

    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link")


class LoginPageLocators:

    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")


class ProductsPageLocators:
    ADD_TO_CART_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
