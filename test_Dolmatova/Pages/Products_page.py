from .Base_page import BasePage
from .locators import ProductsPageLocators


class ProductsPage(BasePage):
    def should_be_view_products(self):
        assert "inventory" in self.browser.current_url, "wrong url"

    def add_item_to_cart(self):
        self.browser.find_element(*ProductsPageLocators.ADD_TO_CART_BACKPACK).click()

    def item_added_to_cart(self):
        assert self.element_is_presented(*ProductsPageLocators.CART_BADGE)
        assert self.element_is_presented(*ProductsPageLocators.REMOVE_BUTTON)

    def no_item_in_cart(self):
        assert self.element_is_not_presented(*ProductsPageLocators.CART_BADGE)
        assert self.element_is_not_presented(*ProductsPageLocators.REMOVE_BUTTON)

    def remove_item_from_cart(self):
        self.browser.find_element(*ProductsPageLocators.REMOVE_BUTTON).click()
