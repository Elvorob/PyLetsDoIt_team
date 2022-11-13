import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_login_pu():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://www.saucedemo.com/")
    login_pu = browser.find_element(By.ID, "user-name")
    login_pu.send_keys("problem_user")

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    time.sleep(2)

    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)

    browser.quit()



