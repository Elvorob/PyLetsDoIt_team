import pytest

from Pages.login_page import *


@pytest.fixture(scope="class")
def driver():
    print("\n start browser....")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    print("\n quit browser")
    driver.quit()


def test_add_to_cart_check_item(driver):
    page = LoginPage(driver, link)
    page.login_password()
    assert driver.title == "Swag Labs", "____YOU NOT ENTER______"
    time.sleep(2)
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(2)
    assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Test.allTheThings() T-Shirt (Red)", 'NOT FOUND'
    time.sleep(2)

