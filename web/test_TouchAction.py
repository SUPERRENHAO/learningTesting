from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class Test_TouchAction():
    # 手机模式
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # 如果报W3C的错误，需要改一下chromweb的配置
    def setup(self):
        # 报W3C的错误，可以使用一下的方法进行解决
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    # 滑动到底部
    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")

        input_element = self.driver.find_element(By.ID,"kw")
        input_element.send_keys("selenium测试")
        search_element = self.driver.find_element(By.ID,"su")

        action = TouchActions(self.driver)
        action.tap(search_element)
        action.perform()
        # 滑动到底部，以search_element为由，响下滑动10000，保证不同浏览器都可以滑动到底部
        action.scroll_from_element(search_element,0,10000).perform()
        sleep(3)

    # 表单操作
    


if __name__ == '__main__':
    pytest.main()
