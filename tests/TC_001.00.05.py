from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)

"""TC_001.00.05| Login Page >
User is unable to login with empty username and password"""


def test_login_page_with_empty_fields():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    assert (
        driver.find_element(
            By.XPATH, '//h3[text() = "Epic sadface: Username is required"]'
        )
        and driver.current_url == "https://www.saucedemo.com/"
    )


def test_login_page_with_empty_fields_2():
    driver.get("https://www.saucedemo.com/")
    user_name = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    assert user_name.get_attribute("value") == ""
    assert password.get_attribute("value") == ""

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    assert (
        driver.find_element(
            By.XPATH, '//h3[text() = "Epic sadface: Username is required"]'
        )
        and driver.current_url == "https://www.saucedemo.com/"
    )
