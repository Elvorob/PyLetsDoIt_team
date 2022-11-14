from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_presented(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def element_is_not_presented(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return True
        return False

    def should_be_authorized_user(self):
        assert self.element_is_presented(*BasePageLocators.CART_ICON)
