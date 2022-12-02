from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class loginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    user_name = (By.ID, "user-name")

    password = (By.ID, "password")

    login_btn = (By.ID, "login-button")

    def get_user(self):
        return self.driver.find_element(*self.user_name)

    def get_pass(self):
        return self.driver.find_element(*self.password)

    def login(self):
        return self.driver.find_element(*self.login_btn)

