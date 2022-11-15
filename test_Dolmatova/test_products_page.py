import time
from .Pages.Login_page import LoginPage
from .Pages.Products_page import ProductsPage

link = "https://www.saucedemo.com/"


class TestProductsPage:
    def test_user_is_authorized(self, browser):
        page = LoginPage(browser, link)
        page.open_page()
        time.sleep(2)
        page.log_in_to_account()
        time.sleep(2)
        page.should_be_authorized_user()

    def test_add_item_in_the_cart(self, browser):
        page = LoginPage(browser, link)
        page.open_page()
        time.sleep(2)
        page.log_in_to_account()
        time.sleep(2)
        page.should_be_authorized_user()
        page = ProductsPage(browser, link)
        page.should_be_view_products()
        page.add_item_to_cart()
        time.sleep(2)
        page.item_added_to_cart()

    def test_remove_item_from_the_cart(self, browser):
        page = LoginPage(browser, link)
        page.open_page()
        time.sleep(2)
        page.log_in_to_account()
        time.sleep(2)
        page.should_be_authorized_user()
        page = ProductsPage(browser, link)
        page.should_be_view_products()
        page.no_item_in_cart()
        page.add_item_to_cart()
        page.item_added_to_cart()
        page.remove_item_from_cart()
        page.no_item_in_cart()
