import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Config.config import TestData
from webdriver_manager.chrome import ChromeDriverManager
#from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request):
    chromedrivermanager =ChromeDriverManager()
    if request.param == "chrome":
        #chrome_options = ChromeOptions()
        #chrome_options.add_argument("--disable-infobars")
        #chrome_options.add_argument("--proxy-server=127.0.0.1")
        web_driver = webdriver.Chrome(chromedrivermanager.install())
        #web_driver = webdriver.Chrome(executable_path ='/usr/local/bin/chromedriver')
        request.cls.driver = web_driver
        yield
        web_driver.close()
        #executable_path = TestData.CHROME_EXECUTABLE_PATH