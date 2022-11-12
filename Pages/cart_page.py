from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from common.Selectors import *
from Pages.base_page import *


link = "https://www.saucedemo.com/"


class CartPage(BasePage):
    def setup(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def click_icon_cart(self):
        self.browser.find_element(*CartLocators.CART_ICON).click()

    def teardown(self):
        self.browser.quit()
