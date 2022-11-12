import pytest


from Pages.login_page import *
from Pages.cart_page import *


@pytest.fixture(scope="class")
def driver():
    print("\n start browser....")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    print("\n quit browser")
    driver.quit()


@pytest.mark.xfail(rises="NotWorking")
def test_change_qty(driver):
    page = LoginPage(driver, link)
    page.login_password()
    assert driver.title == "Swag Labs", "____YOU NOT ENTER______"
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    time.sleep(3)
    cart = CartPage(driver, link)
    cart.click_icon_cart()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]").click()

    time.sleep(3)
