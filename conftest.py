import pytest
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://www.saucedemo.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):

            # only add additional html on failure
            extra.append(pytest_html.extras.image(""))
        report.extra = extra