# TC_001.00.04 | Login Page > Verify login with valid password (performance_glitch_user)

# Environment and Test Data:
# Please, choose: Web Version
#
# Test Data
# Username: performance_glitch_user
# Password: secret_sauce
#
# PRECONDITIONS:
# Log in to https://www.saucedemo.com/
#
# STEPS:
#
# Enter Username.
# Enter Password
# Click [Login]
# Expected result:
# The Products page will open.
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link_main = "https://www.saucedemo.com/"


def test_username():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link_main)

    assert driver.title == "Swag Labs"
    enter_username = driver.find_element(By.ID, "user-name")
    enter_username.send_keys("problem_user")
    enter_password = driver.find_element(By.ID, "password")
    enter_password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    assert "inventory" in driver.current_url
