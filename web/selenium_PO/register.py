from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:

    def __init__(self,driver:WebDriver):
        self._driver = driver

    def register(self):
        sleep(3)
        self._driver.find_element(By.ID,'corp_name').send_keys("企业微信注册")
        self._driver.find_element(By.ID,'manager_name').send_keys("用户名信息")
        sleep(3)
        self._driver.quit()

        return  True

