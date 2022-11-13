import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_logout_standard_user():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://www.saucedemo.com")
    login_su = browser.find_element(By.ID, "user-name")
    login_su.send_keys("standard_user")

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    time.sleep(1)
    browser.find_element(By.ID, "login-button").click()
    assert "inventory" in browser.current_url
    browser.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)

    browser.find_element(By.ID, "logout_sidebar_link").click()
    assert "saucedemo.com" in browser.current_url
    time.sleep(1)

    browser.quit()
