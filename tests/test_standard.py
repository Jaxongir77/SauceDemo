import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.cartPage import cartPage
from pageObject.checkOutInfo import CheckOut
from pageObject.checkOutOverview import checkOver
from pageObject.loginPage import loginPage
from pageObject.productPage import productPage
from tests.conftest import data_load
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


@pytest.mark.ui
class TestStandard(BaseClass):
    def test_standard(self, data_load):
        loginP = loginPage(self.driver)

        wait = WebDriverWait(self.driver, 10)

        loginP.get_user().send_keys(data_load["username"])

        loginP.get_pass().send_keys(data_load["password"])

        wait.until(expected_conditions.element_to_be_clickable(loginP.login()))
        loginP.login().click()

        product = productPage(self.driver)

        select = Select(product.get_select())

        select.select_by_value("hilo")

        products = product.get_cart()

        for items in products:
            items.click()

        product.get_cart_button().click()

        cart = cartPage(self.driver)

        cart.get_check().click()

        checkout = CheckOut(self.driver)

        checkout.get_first_name().send_keys(data_load["first"])

        checkout.get_last_name().send_keys(data_load["last"])

        checkout.get_zip().send_keys(data_load["zip"])

        checkout.get_cont().click()

        check_over = checkOver(self.driver)

        check_over.get_finish().click()

        checkout.get_home().click()

        product.get_menu().click()

        product.get_logout().click()
