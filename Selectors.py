from selenium.webdriver.common.by import By

URL = "https://www.saucedemo.com/"


class LoginPageLocators():
    USER_NAME = (By.XPATH_SELECTOR, 'id')

# class LoginPageLocators():
#     LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
#     REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
#     REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
#     REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
#     CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
#     REG_BTN = (By.XPATH, "//form[@id='register_form']//button")
