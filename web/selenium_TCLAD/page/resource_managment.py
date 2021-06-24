from time import sleep

from selenium.webdriver.common.by import By

from web.selenium_TCLAD.page.base_page import Base_Page


class Resource_managment(Base_Page):

    def click_list(self):
        # 封装操作
        self.find(By.CSS_SELECTOR, '#tree-div>div>div:nth-child(3) .eleTree-node-content-icon').click()
        self.find(By.CSS_SELECTOR,
                  '#tree-div>div>div.eletree-node-group>div:first-child>div:nth-child(3)>span:first-child').click()
        self.find(By.XPATH, '//*[@id="tree-div"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/i').click()
        self.find(By.XPATH,
                  '//*[@id="tree-div"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/i').click()
        self.find(By.XPATH, '//*[@id="tree-div"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]').click()

        # 添加参数
    def sendkey(self):
        self.find(By.CSS_SELECTOR, '.pageBack > a:nth-child(1)').click()
        self.find(By.ID, 'globalId').send_keys('TCL1')
        self.find(By.ID, 'mediaName').send_keys('TCL1')
        self.action_select(self.finds(By.XPATH, '//*[@id="mediaType"]')[2])
        self.find(By.CSS_SELECTOR, '.btOk').click()

    def add_resource(self):

        # self.find(By.CSS_SELECTOR,'.icon-rotate').click()
        # //*[@id="tree-div"]/div/div[1]/span[1]/i
        # elements = self.finds(By.XPATH,'//*[@id="tree-div"]/div/div[1]/span[1]')
        # for elment in elements:
        #     elment.click()

        # self.find(By.XPATH,'//*[@id="tree-div"]/div/div[1]/span[1]/i').click()
        # self.find(By.CSS_SELECTOR,'').click()
        # CSS定位
        # self.find(By.CSS_SELECTOR,'#tree-div>div>div:nth-child(3) .eleTree-node-content-icon').click()
        # self.find(By.CSS_SELECTOR,'#tree-div>div>div.eletree-node-group>div:first-child>div:nth-child(3)>span:first-child').click()
        # self.find(By.XPATH,'//*[@id="tree-div"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/i').click()
        # self.find(By.XPATH,'//*[@id="tree-div"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/i').click()
        # self.find(By.XPATH,'//*[@id="tree-div"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]').click()
        # self.find(By.LINK_TEXT,'欢网科技').click()
        self.click_list()

        self.switch_Frame('nodeIframe')

        self.sendkey()

        self.switch_default_content()

        # self.find(By.CSS_SELECTOR,'.pageBack > a:nth-child(1)').click()
        # self.find(By.ID,'globalId').send_keys('TCL1')
        # self.find(By.ID,'mediaName').send_keys('TCL1')
        # #mediaType
        # print(len(self.finds(By.ID, 'mediaType')))

        # self.wait_for_click(self.find(By.CSS_SELECTOR,'.btOk'))

        #// *[ @ id = "mediaType"]
        # opt = self.find(By.LINK_TEXT,'APP广告')
        # elments = self.finds(By.XPATH,'//*[@id="mediaType"]')
        # print(len(elments))
        # self.action_select(self.finds(By.XPATH,'//*[@id="mediaType"]')[2])
        #
        # self.find(By.CSS_SELECTOR,'.btOk').click()

    def get_resource(self,result):
        self.click_list()
        # 获取在该列表下所有test

        sleep(2)
        elements = self.finds(By.XPATH,
                              '//*[@id="tree-div"]/div/div[2]/div[1]/div[2]//span[@class="eleTree-node-content-label"]')
        # self.wait_for_click(elements[-1])

        # elements = self.finds(By.XPATH,'//*[@id="tree-div"]/div/div[2]/div[1]/div[2]//span[@class="eleTree-node-content-label"]')

        for element in elements:
            # list.append(element.get_attribute('title'))
            if result == element.text:
                # print(element.get_attribute('title'))
                # list.append(result)
                return True

        return False

