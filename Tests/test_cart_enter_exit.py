from common.Selectors import *


def test_open_cart(driver, correct_login):
    assert driver.title == "Swag Labs", "NOT ENTER"
    driver.find_element(*CartLocators.CART_ICON).click()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"
    driver.find_element(*CartLocators.CONTINUE_SHOPPING).click()
    assert driver.title == "Swag Labs", "____You NOT LEFT_____"
    driver.quit()
