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


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url(browser.current_url))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.split('::')[-1] + ".png"
#             file_name_ = "." + directory + file_name
#             file_name_html = 'assets/' + file_name
#             browser.get_screenshot_as_file(file_name_)
#             if file_name_:
#                 html = f"<div><img src='{file_name_html}' alt='screenshot'"
#                 html += "onclick='window.open(this.src)' style='width:400px;'"
#                 html += " align='right'/></div>"
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra


# or


#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         extra.append(pytest_html.extras.url(driver.current_url))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
#             driver.get_screenshot_as_file('screens/screenshot-%s.png' % test_name)
#             extra.append(pytest_html.extras.image('screens/screenshot-%s.png' % test_name))
#         report.extra = extra
