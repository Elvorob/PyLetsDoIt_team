# TC_001.00.06| Login Page > User is unable to login with wrong username and correct password
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link_main = "https://www.saucedemo.com/"


def test_wrong_username():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link_main)
    assert browser.title == "Swag Labs"

    enter_username = browser.find_element(By.ID, "user-name")
    enter_username.send_keys("abrakadabra")
    enter_password = browser.find_element(By.ID, "password")
    enter_password.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)
    assert "https://www.saucedemo.com/" in browser.current_url

    enter_username.send_keys([Keys.BACK_SPACE] * 20)
    enter_password.send_keys([Keys.BACK_SPACE] * 20)
    time.sleep(2)
    enter_username.send_keys("standard_user")
    enter_password.send_keys("secret_sauce")
    login_button.click()
    time.sleep(2)
    assert "inventory" in browser.current_url
