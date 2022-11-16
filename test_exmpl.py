import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


def test_sort_dropdown():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://www.saucedemo.com/")

    assert browser.title == "Swag Labs"
    enter_username = browser.find_element(By.ID, "user-name")
    enter_username.send_keys("standard_user")
    enter_password = browser.find_element(By.ID, "password")
    enter_password.send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)
    el = browser.find_element(By.CLASS_NAME, "product_sort_container")
    el.click()
    time.sleep(2)
    # element = browser.find_element(By.XPATH, "//option[contains(text(),'Name (Z to A)')]")
    # element.click()
    print(el.is_enabled())
