import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Common.Selectors import *

# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture(scope="function")
# def driver():
#     o = webdriver.ChromeOptions()
#     o.headless = True
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()), options=o
#     )
#     yield driver
#
#     driver.quit()
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver


def test_open_cart(driver):
    driver.get(link)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    driver.find_element(By.ID, "shopping_cart_container").click()
    print("___You IN Product Cart____")
    assert driver.current_url == "https://www.saucedemo.com/cart.html"
    driver.find_element(By.ID, "continue-shopping").click()
    print("______LEFT THE CART_____")
    assert driver.title == "Swag Labs"
    time.sleep(2)

    driver.quit()
