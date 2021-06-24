from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page():
    _driver:WebDriver = None
    _base_url = ""

    # 初始化
    def __init__(self,driver:WebDriver = None):
        if driver is None:
            print("只有第一次是空的")
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    # 定位元素
    def find(self,by,locator):

        return self._driver.find_element(by,locator)

    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)

    def switch_Frame(self,ID):
        return self._driver.switch_to.frame(ID)

    def switch_default_content(self):
        return self._driver.switch_to.default_content()

    def action_select(self,locator,value = None):

        return Select(locator).select_by_index(1)

    def quit(self):
        self._driver.quit()

    def wait_for_click(self,locartor,time = 10):
        WebDriverWait(self,time).until(expected_conditions.element_to_be_clickable(locartor))