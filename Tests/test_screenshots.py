import time
from selenium.webdriver.common.by import By


def test_screen_html(driver, correct_login):
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "logout_sidebar_link").click()
