from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class cartPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    check_out = (By.ID, "checkout")

    def get_check(self):
        return self.driver.find_element(*self.check_out)