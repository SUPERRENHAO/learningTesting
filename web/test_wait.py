from time import sleep
from selenium import webdriver
# 底层的查找元素
from selenium.webdriver.common.by import By
# 内置查看元素
from selenium.webdriver.support import expected_conditions
# 显示等待
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        # 隐式等待
        # 隐式等待有个弊端，就是隐式等待只管这个元素，而不会管这个这个元素是否可以点击，所以解决这个问题，需要用到显示等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("霍格沃滋测试学院")
        self.driver.find_element(By.CSS_SELECTOR,'#su').click()
        sleep(3)

    def test_wait123(self):

        print("hellp")
        self.driver.find_element(By.XPATH,'//*[@title="原创精华文章,有100元奖金"]').click()

        # 判断函数
        # 但是一定要注意一下，这个判断函数一定要有参数，
        def wait(x):
            return  len(self.driver.find_elements(By.XPATH,'//*[@class="default"]')) >= 1

        # python内置的一些写好的条件
        # expected_conditions.element_to_be_clickable(传入需要查看的元素) 这是python写好的一些方法，
        # 查看元素可否点击element_to_be_clickable 以及是否存在页面，都在这个库里面可以找到
        find_elent = (By.XPATH,'//*[@class="posts sortable num"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(find_elent))
        # WebDriverWait(self.driver,10).until(wait())

        # 显示等待 ----需要等待的浏览器，等待的时间，后面加等待的条件，需要传入一个函数
        # WebDriverWait(self.driver,10).until(wait)

        self.driver.find_element(By.XPATH, '//*[@title="有新帖的话题"]').click()
        # self.driver.find_element_by_link_text("测试人生 | 从外包菜鸟到测试开发，薪资一年翻三倍，连自己都不敢信！（附面试真题与答案）").click()

