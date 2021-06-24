from time import sleep

from selenium.webdriver.common.by import By

from web.selenium_windowAndFrame.base import Base


class Test_frame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

        # 切换frame 需要传入frame的id。来进行切换
        self.driver.switch_to.frame('iframeResult')
        # 这两种切换效果是一样的
        # self.driver.switch_to_frame('iframeResult')
        print(self.driver.find_element(By.ID, 'draggable').text)
        # 切换到父级frame
        # self.driver.switch_to.parent_frame()
        # 切换到默认frame
        self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, 'submitBTN').text)
        sleep(3)