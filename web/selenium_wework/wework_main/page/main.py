from selenium.webdriver.common.by import By

from web.selenium_wework.wework_main.page.base_page import BasePage
from web.selenium_wework.wework_main.page.member import Member


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = '127.0.0.1:9222'
    #     self._driver = webdriver.Chrome(options=options)


    def goto_tongxunle(self):

        self.find(By.ID,'menu_contacts').click()

        return Member(self._driver)