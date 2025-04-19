from time import sleep
from selenium import webdriver
from pytest import fixture
from POMpages.loginpage import LoginPage
@fixture
def set_tear():
    driver=webdriver.Chrome()
    driver.get("https://shoppersstack.com/")
    driver.maximize_window()
    sleep(30)
    yield driver
    driver.quit()
@fixture
def login(set_tear):
    login=LoginPage(set_tear)
    login.login()
    return set_tear