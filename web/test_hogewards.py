from time import sleep

from selenium import webdriver


class TestHogewards():
    def setup(self):
        # 打开浏览器
        self.drvice = webdriver.Chrome()
        # 浏览器最大化
        self.drvice.maximize_window()
        # 隐式等待
        self.drvice.implicitly_wait(5)

    def teardown(self):
        self.drvice.quit()

    def test_hogewards(self):
        self.drvice.get("https://testerhome.com/")
        self.drvice.find_element_by_css_selector("#main-nav-menu > .nav-item:nth-child(1) > .nav-link").click()
        self.drvice.find_element_by_css_selector(".topic-30283 .title > a").click()
