from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_From():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_quit(self):
        self.driver.get("https://testerhome.com/account/sign_in")

        username = self.driver.find_element(By.ID,'user_login')
        username.send_keys("123")

        password = self.driver.find_element(By.ID,'user_password')
        password.send_keys("456")

        # self.driver.find_element_by_id('user_remember_me').click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        # remember_me = self.driver.find_element(By.CSS_SELECTOR,'#user_remember_me')
        # remember_me.click()
        #
        # login = self.driver.find_element((By.CSS_SELECTOR,'#new_user > div.form-actions > input'))
        # login.click()
        sleep(3)


if __name__ == '__main__':
    pytest.main()
