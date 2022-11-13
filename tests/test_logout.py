import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link_main = "https://www.saucedemo.com/"


def test_logout():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link_main)

    assert browser.title == "Swag Labs"
    enter_username = browser.find_element(By.ID, "user-name")
    enter_username.send_keys("problem_user")
    enter_password = browser.find_element(By.ID, "password")
    enter_password.send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)

    browser.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    browser.find_element(By.ID, "logout_sidebar_link").click()
    assert browser.current_url == "https://www.saucedemo.com/"
