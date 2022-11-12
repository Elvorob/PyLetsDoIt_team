import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Common.Selectors import *
from Pages.base_page import *

link = "https://www.saucedemo.com/"


class LoginPage(BasePage):
    def setup(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_open_link(self):
        self.browser.get(link)

    def login_password(self):
        self.browser.get(link)
        self.browser.find_element(*Loginlocators.BOX_LOGIN).send_keys(*Loginlocators.USER_NAME)
        self.browser.find_element(*Loginlocators.BOX_PASSWORD).send_keys(*Loginlocators.PASSWORD)
        self.browser.find_element(*Loginlocators.BT_LOGIN).click()
        time.sleep(2)

    def teardown(self):
        self.browser.quit()
