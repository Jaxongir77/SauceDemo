from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


class productPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    # add to card buttons

    add_cart = (By.XPATH, "//button[text()='Add to cart']")

    selector = (By.XPATH, "//select[@class='product_sort_container']")

    cart_button = (By.XPATH, "//a[@class='shopping_cart_link']")

    logout = (By.XPATH, "//a[text() = 'Logout']")

    menu = (By.ID, "react-burger-menu-btn")



    def get_cart(self):
        return self.driver.find_elements(*self.add_cart)

    def get_select(self):
        return self.driver.find_element(*self.selector)

    def get_cart_button(self):
        return self.driver.find_element(*self.cart_button)

    def get_logout(self):
        return self.driver.find_element(*self.logout)

    def get_menu(self):
        return self.driver.find_element(*self.menu)
