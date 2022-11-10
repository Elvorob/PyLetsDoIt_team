from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

link = "https://www.saucedemo.com/"


def test_user_is_authorized():
    o = webdriver.ChromeOptions()
    o.headless = True
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=o)
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "#user-name")
    input1.send_keys("standard_user")
    input2 = browser.find_element(By.CSS_SELECTOR, "#password")
    input2.send_keys("secret_sauce")
    button = browser.find_element(By.CSS_SELECTOR, "#login-button")
    button.click()
    browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    browser.quit()
