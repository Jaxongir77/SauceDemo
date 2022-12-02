from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class CheckOut(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    fname = (By.ID, "first-name")
    lname = (By.ID, "last-name")
    zip = (By.ID, "postal-code")
    cont = (By.ID, "continue")

    home = (By.ID, "back-to-products")

    def get_first_name(self):
        return self.driver.find_element(*self.fname)

    def get_last_name(self):
        return self.driver.find_element(*self.lname)

    def get_zip(self):
        return self.driver.find_element(*self.zip)

    def get_cont(self):
        return self.driver.find_element(*self.cont)

    def get_home(self):
        return self.driver.find_element(*self.home)

