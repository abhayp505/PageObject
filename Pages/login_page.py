from selenium.webdriver.common.by import By

from Config.config import TestData
from utilities.SeleniumUtilities import BasePage

class LoginPage(BasePage):

    USER_NAME = (By.NAME, "username")
    USER_NAME_BUTTON = (By.CLASS_NAME, "moat-button")
    PASS_WORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "moat-button")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(TestData.BASE_URL)


    def login_opsweb(self, username, password):
        self.send_keys(self.USER_NAME, username)
        self.click(self.USER_NAME_BUTTON)
        self.send_keys(self.PASS_WORD, password)
        self.click(self.LOGIN_BUTTON)
