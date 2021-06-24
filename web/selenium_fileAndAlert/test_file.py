from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from web.selenium_fileAndAlert.base import Base


# 使用调用js来添加image属性
def exceute_script_bases(self,js_pha,locator):
    js = 'arguments[0].style.display = "block";'
    locator = ('xpath','ele_xpath')
    # driver = webdriver.Chrome()
    ele = self.driver.find(locator)
    self.driver.execute_script(js_pha,locator)
    ele.send_keys('filepath')


class Test_fileAndAlert(Base):
    @pytest.mark.skip
    def test_file(self):
        self.driver.get('https://iamge.baidu.com/')
        self.driver.find_element(By.ID,'sttb').click()
        fileElement = self.driver.find_element(By.XPATH,'//*[@id="dttip"]')
        # 如果是input的标签可以直接使用这种方式上传图片
        fileElement.send_keys("./Users/ninhiroshi/Desktop/未命名文件夹/学习的12期/web/selenium_fileAndAlert/test.jpg")
        sleep(10)

    # 在这个https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable网址上
    # 1、将元素1拖拽到元素2
    # 2、切换到alert点击确认
    # 3、点击开始
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        drag = self.driver.find_element(By.ID,'draggable')
        drop = self.driver.find_element(By.ID,'droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform() # 注意一定要开始动画
        text = self.driver.switch_to_alert().text
        print(text)
        sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID,'submitBTN').click()
        sleep(3)


