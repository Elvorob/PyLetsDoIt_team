# TC_005.02.01 | gumburger menu > All items
# STEPS:
# 1. After authorization, you should be on products list page: https://www.saucedemo.com/inventory.html
# 2. Select any item in the list
# 3. Made left click and open the item page
# 4. On new page click ALL ITEMS in main menu
# 5. Make sure that you are on products list page: https://www.saucedemo.com/inventory.html again
#
# EXPECTED RESULTS:
# User should see https://www.saucedemo.com/inventory.html page
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link_main = "https://www.saucedemo.com/"


def test_hamburger_menu():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link_main)

    enter_username = driver.find_element(By.ID, "user-name")
    enter_username.send_keys("standard_user")
    enter_password = driver.find_element(By.ID, "password")
    enter_password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "inventory" in driver.current_url
    a = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(a) == 6
    a[0].click()
    time.sleep(2)
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "inventory_sidebar_link").click()
    assert "inventory" in driver.current_url
