from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class checkOver(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    finish = (By.ID, "finish")

    def get_finish(self):
        return self.driver.find_element(*self.finish)