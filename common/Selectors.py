from selenium.webdriver.common.by import By

link = "https://www.saucedemo.com/"


class Loginlocators():
    BOX_LOGIN = (By.ID, "user-name")
    USER_NAME = "standard_user"
    BOX_PASSWORD = (By.ID, "password")
    PASSWORD = "secret_sauce"
    BT_LOGIN = (By.ID, "login-button")

class CartLocators():
    CART_ICON = (By.ID, "shopping_cart_container")
    BT_CHECKOUT = (By.ID, "checkout")
    CONTINUE_SHOPPING =(By.ID, "continue-shopping")
