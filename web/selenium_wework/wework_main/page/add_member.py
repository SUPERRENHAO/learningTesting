from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.selenium_wework.wework_main.page.base_page import BasePage


class Add_member(BasePage):
    # def __init__(self,driver :WebDriver):
    #     self._driver = driver

    def add_member(self):
        # sleep(3)
        self.find(By.ID,'username').send_keys("9atest_case1")
        self.find(By.ID,'memberAdd_acctid').send_keys("9atest_case1")
        self.find(By.ID,'memberAdd_phone').send_keys('13877332342')
        # self._driver.find_element(By.XPATH,'//*[@id="js_contacts78"]/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
        # sleep(3)
        self._driver.find_elements_by_link_text("保存")[0].click()

        sleep(3)
        return True

    def update_page(self):
        content_text: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        return [int(x) for x in content_text.split('/',1)]
    # 断言
    def get_member(self,value):
        # elements = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td')

        # content_text:str = self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
        # # 使用切割的方法，分割字符串
        # cur_page, total_page = content_text.split('/',1)

        # list = []
        # for element in elements:
        #     list.append(element.get_attribute("title"))
        # return  list
        # 上吗这种方式也可以写成这样 这是python的特性
        # return [element.get_attribute('title') for element in elements]
        # 显示等待到该元素可以找到
        self.wiat_for_click((By.CSS_SELECTOR, '.ww_checkbox'))
        cur_page,total_page = self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td')
            for element in elements:
                # 如果在页面中找到这个元素，就返回ture
                if value == element.get_attribute('title'):
                    return True
                # 如果在当前页面没有找到这个元素，就继续用往下找
                # 刷新这个值
                cur_page = self.update_page()[0]
            if cur_page == total_page:
                return False
            # 下一页
            self.find(By.CSS_SELECTOR,'.js_next_page').click()





