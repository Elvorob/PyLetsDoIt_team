import pytest
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from common.Selectors import *


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def correct_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(*Loginlocators.BOX_LOGIN).send_keys(Loginlocators.USER_NAME)
    driver.find_element(*Loginlocators.BOX_PASSWORD).send_keys(Loginlocators.PASSWORD)
    driver.find_element(*Loginlocators.BT_LOGIN).click()
    assert driver.title == "Swag Labs", "____YOU NOT ENTER______"
    time.sleep(2)

