# 倒入基础类
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from web.selenium_windowAndFrame.base import Base



class Test_windowAndFrame(Base):

    # 需求，从百度注册切换到百度登陆
    def test_wondow(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID,'s-top-loginbtn').click()
        sleep(3)
        # self.driver.find_element(By.LINK_TEXT,'立刻注册').click()
        self.driver.find_element(By.CSS_SELECTOR,'#passport-login-pop-dialog > div > div > div > div.tang-pass-footerBar > a').click()
        # 切换窗口
        # 1、获取当前的窗口
        # 2、获取所有窗口
        # 3、switch_to对应窗口
        cuuent_window = self.driver.current_window_handle
        windows = self.driver.window_handles
        #  切换窗口
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_4__userName').send_keys("1234456")
        self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_4__phone').send_keys("123000982223")
        sleep(3)
        self.driver.switch_to.window(cuuent_window)
        # self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__footerQrcodeBtn').click()
        # 使用用户名登陆
        self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__userName').send_keys("username")
        self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__password').send_keys("123456777")
        self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__submit').click()
        sleep(3)



if __name__ == '__main__':
    pytest.main('-v','-s')
