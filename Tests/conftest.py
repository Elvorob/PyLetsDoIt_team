import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    yield driver
    driver.quit()
