import os
from selenium import webdriver


class Base():
    def setup(self):

        # 做兼容性测试的时候
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

        # 调用的时候传入browser参数即可
        # browser = chrome pytest test_frame.py

        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()