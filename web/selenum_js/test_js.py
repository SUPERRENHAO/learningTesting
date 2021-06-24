from time import sleep

import pytest
from selenium.webdriver.common.by import By

from web.selenium_windowAndFrame.base import Base


class Test_JS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID,'kw').send_keys("selenium测试")
        # 使用js获取元素
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()

        # 滑动到底部
        self.driver.execute_script('document.documentElement.scrollTop = 100000')
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,'#page > div > a.n').click()
        sleep(3)

        # 常用的JS
        # for code in [
        #     # 第一个是发挥标题，第二个是返回对应的数据时间，用于性能数据分析
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
            # print(self.driver.execute_script(code))
        # 也可以这样实现
        # 但是这种会有一个情况发生，那就是只会返回第一个执行代码的值，后面的不糊返回来
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_removeA(self):
        self.driver.get('https://www.12306.cn/index/')
        # 获得元素属性并去掉readonly属性
        elemennt = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute = 'readonly'")
        # self.driver.execute_script("removeAttribute = 'readonly'")
        # 对元素进行赋值操作
        self.driver.execute_script("document.getElementById('train_date').value='2021-07-29'")
        sleep(3)