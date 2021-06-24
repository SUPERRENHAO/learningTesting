from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.selenium_wework.wework_main.page.add_member import Add_member
from web.selenium_wework.wework_main.page.base_page import BasePage


class Member(BasePage):
    # def __init__(self,driver :WebDriver):
    #     self._driver = driver




    def goto_addMember(self):

        # sleep(3)
        # css_str = '#js_contacts105 > div > div.member_colRight > div > div.js_party_info > div.js_has_member > div:nth-child(1) > a.qui_btn.ww_btn.js_add_member'
        # self._driver.find_element(By.CSS_SELECTOR,css_str).click()
        # self._driver.find_element_by_link_text("添加成员").click()
        # css 层级定位
        # self._driver.find_element(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1) .js_add_member').click()

        # 启用显示等待
        # 不加上这个显示等待，会出现该元素已出现，但是无法点击的操作，
        locator = (By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)')
        self.wiat_for_click(locator)
        self.find(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()

        return Add_member(self._driver)


