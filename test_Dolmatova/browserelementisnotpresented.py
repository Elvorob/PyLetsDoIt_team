from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def element_is_not_presented(method, locator):
    o = webdriver.ChromeOptions()
    o.headless = True
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=o
    )
    try:
        browser.find_element(method, locator)
    except NoSuchElementException:
        return True
    return False
