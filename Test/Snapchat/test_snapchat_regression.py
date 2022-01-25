import time

# from Test.test_base import BaseTest
from Pages.login_page import LoginPage
from Test.test_base import BaseTest


class TestLogin(BaseTest):

    def test_opsweb_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_opsweb("ops_web_test_user@oracle.com", "Password@123")
        time.sleep(10)

    # def test_opsweb_login1(self):
    #     print("Helllo World!!")
    #     time.sleep(10)