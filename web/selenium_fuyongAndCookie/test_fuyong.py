import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestFuyong():
    def setup(self):
        # # 复用调试浏览器,注意不要多浏览器
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_fuyong(self):
        # 获取cookile----使用浏览器复用来获得当前页面的cookie
        # cookiles = self.driver.get_cookies()
        # print(cookiles)
        cookiles_tmp = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'iTLGvG4OeFm-AF6ealRZXVVS80pQf2HdB81_-CskWGO9OIXXb1VHIuHlfl-UHK9cYHBEb5ulYDfaJ-1yishCND7wbGaYEWhCVCHcwiKTzcMteuduTAiIBwJYooCF0bhSJ54Pa8YkWi9sK7IFPQj7-RFzhxbDOfJBOBbNEELfCst1XHz18ife2l7JMK6c_48sBs5wBdw7IzgdSuEche_xiecj6m3Vo_v1pGAYOrRK7GXDv3MZOeAM4r3iBOLN4baUVUytj3Dit9e1fCq0Ry4J4A'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850237958971'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325103473515'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'coZr4ZVWQa9YafNheE9kKkJT-dazGcPnmi-yX3mDwk5pkiOMxi8JAl2c2viY8ct5'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9322863'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1655823991, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1624253783,1624287992'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '1566875555'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1687360006, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.924971300.1624253783'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1655789781, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1624318225, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': 'hgqbge'},
            {'domain': '.qq.com', 'expiry': 1624374406, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.211632190.1624253783'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850237958971'},
            {'domain': '.qq.com', 'expiry': 1938615057, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False,
             'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1626880009, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1624287992'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '197140795393344'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '620356608'},
            {'domain': '.qq.com', 'expiry': 1887290737, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5db1c270b7681'}]
        # 使用shelve保存cookie
        # 1、使用复用技术获得当前的网页的cookie
        # 2、使用shelve来保存这个cookie
        # 3、使用这个cookie
        db = shelve.open('cookies')
        # db['cookie'] = self.driver.get_cookies()

        cookiles = db['cookie']
        # 使用前后，都需要调用打开一遍这个窗口
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # 对cookie进行处理
        for cookile in cookiles:
            if 'expiry' in cookile.keys():
                cookile.pop("expiry")
            self.driver.add_cookie(cookile)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.add_cookie()
        db.close()