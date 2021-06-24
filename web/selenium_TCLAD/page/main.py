from selenium.webdriver.common.by import By

from web.selenium_TCLAD.page.base_page import Base_Page
from web.selenium_TCLAD.page.launcher import Launcher


class Main(Base_Page):

    _base_url = "http://adms.ads.huantest.com/adms/index.do"
    _loginstate = False
    def login(self):
        self.find(By.ID,'username').send_keys('tcl')
        self.find(By.ID,'password').send_keys('QhLjwJlcgNIf')
        self.find(By.ID,'ui_submit').click()


    def goto_launcher(self):

        if self._loginstate == False:
            self.login()
            self._loginstate = True
        return Launcher(self._driver)

