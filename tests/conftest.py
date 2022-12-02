from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest as pytest

from testData.login_data import getData


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_name = request.config.getoption("--browser_name")

    if browser_name == "firefox":

        service_obj = Service("C:\\tools\\selenium\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    if browser_name == "chrome":
        # makes sure that browser stays open after text execution is finished.
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service_obj = Service("C:\\tools\\selenium\\chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=service_obj)

    driver.implicitly_wait(15)

    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver

    yield
    
    sleep(15)
    driver.close()


@pytest.fixture(params=getData.get_data())
def data_load(request):
    print(request.param)
    return request.param
