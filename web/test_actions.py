from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_action():
    def setup(self):
        self.driver = webdriver.Chrome()


    def teardown(self):
        self.driver.quit()

    # 点击用例
    @pytest.mark.skip
    def test_action1(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        elem_click = self.driver.find_element(By.XPATH,'//*[@value="click me"]')
        elem_doubleClick = self.driver.find_element(By.XPATH,'//*[@value="dbl click me"]')
        elem_rightClick = self.driver.find_element(By.XPATH,'//*[@value="right click me"]')
        actions = ActionChains(self.driver)
        actions.click(elem_click)
        actions.context_click(elem_rightClick)
        actions.double_click(elem_doubleClick)
        sleep(3)
        actions.perform()
        sleep(3)

    # 鼠标悬停的方法
    @pytest.mark.skip
    def test_moveto(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        sleep(3)

    # 网页的拖拽事件
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_elemnt = self.driver.find_element(By.XPATH,'//*[@id="dragger"]')
        drop_elemnt = self.driver.find_element(By.XPATH,'/html/body/div[2]')
        actions = ActionChains(self.driver)
        # 这就是拖拽的方法
        # actions.drag_and_drop(drag_elemnt,drop_elemnt).perform()
        # 其内部实现
        # actions.click_and_hold(drag_elemnt).release(drop_elemnt).perform()
        #release() release这个函数，如果传入一个元素给他，他就会移动到这个元素上，如果没有元素给他，他就抬起鼠标左键，释放掉
        # 还有一种方式
        actions.click_and_hold(drag_elemnt).move_to_element(drop_elemnt).release().perform()
        sleep(3)

    # aciton的输入键值，输入一些系统写好的值
    def test_keys(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        element = self.driver.find_element(By.CSS_SELECTOR,'body > label:nth-child(2) > input[type=textbox]')
        element.click()
        action =  ActionChains(self.driver)
        action.send_keys("username").pause(1)
        # ctrl +a 全选
        # action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).pause(2)
        action.key_down(Keys.COMMAND).key_down('a').key_up(Keys.COMMAND).key_up('a').pause(2)
        action.key_down(Keys.COMMAND).key_down('c').key_up(Keys.COMMAND).key_up('c').pause(2)
        action.key_down(Keys.COMMAND).key_down('v').key_up(Keys.COMMAND).key_up('v').pause(2)
        # action.send_keys(Keys.BACK_SPACE).pause(1)
        # action.send_keys("myname").pause(1)
        action.perform()

    # TouchAction针对H5页面的操作，支持手势，ActionChains是模拟鼠标，TouchAction是模拟手势，针对H5页面





if __name__ == '__main__':
    pytest.main("-v","-s")
