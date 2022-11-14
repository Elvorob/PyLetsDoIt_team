from .Base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def log_in_to_account(self):
        username_input = self.browser.find_element(*LoginPageLocators.USER_NAME)
        username_input.send_keys("standard_user")
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys("secret_sauce")
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
