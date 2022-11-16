import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    o = webdriver.ChromeOptions()
    o.headless = True
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=o
    )
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def test_fixture():
    print("\n***first fixture***\n")


def pytest_html_report_title(report):
    report.title = "Anna Dolmatova"
