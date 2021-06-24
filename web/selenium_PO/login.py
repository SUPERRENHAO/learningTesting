from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.selenium_PO.register import Register


class Login():

    def __init__(self,driver:WebDriver):
        self._driver = driver
    def sacnf(self):
        pass

    def goto_register(self):

        self._driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()

        return  Register(self._driver)