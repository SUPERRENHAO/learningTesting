from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 类变量，需要在构造方法前去定值
    _driver = None
    _base_url = ""

    # 构造方法，子类调用的时候，会调用该构造方法
    def __init__(self,driver:WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            # 隐式等待
            self._driver.implicitly_wait(3)
            # 隐式等待有个弊端，就是隐式等待只管这个元素，而不会管这个这个元素是否可以点击，所以解决这个问题，需要用到显示等待

        else:
            self._driver = driver

        if self._base_url != "" :
            self._driver.get(self._base_url)

    # 为了符合PO设计原则，把driver封装起来 但这里封装的很粗糙，需要继续优化
    def find(self,by,locator):
        return  self._driver.find_element(by,locator)

    def finds(self,by,locator):
        return  self._driver.find_elements(by,locator)

    # 显示等待，传入一个元素，判断10s内他是否可以点击
    def wiat_for_click(self,locator, time = 10):

        return WebDriverWait(self._driver,time).until(expected_conditions.element_to_be_clickable(locator))

