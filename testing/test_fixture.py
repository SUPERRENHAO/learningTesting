import pytest

@pytest.fixture()
def login():
    print("需要登陆")
    usrename = "tom"
    yield  usrename
    # 使用yield与fixture结合
    print("teardown方法")

class TestDemo:
    #
    # def setup_class(self):
    #     # 第一步，打开浏览器
    #     print("第一步，打开浏览器")
    #
    # def setup(self):
    #     # 这是方法级别的，每条用例开始的时候都会调用
    #     print("setup")
    #
    #     # 这是方法级别的，每条用例结束的时候都会调用
    # def teardown(self):
    #     print("teardown")
    #
    # def teardown_class(self):
    #     # 这是类级别的teardown，就是只执行一次
    #     # 第五步，关闭浏览器
    #     print("第五步，关闭浏览器")

    def test_a(self,login):
        # 第一步打开浏览器，放在setup中去执行
        # 第二步，输入网址
        # 第三步，定位
        # 第四步，各种操作
        # 第五步，关闭浏览器或者资源回收的操作放在teardown中去执行
        pass

    def test_b(self):
        # 第一步，打开浏览器
        # 第二步，输入网址
        # 第三步，定位
        # 第四步，各种操作
        # 第五步，关闭浏览器
        pass
    def test_c(self,login):
        # 第一步，打开浏览器
        # 第二步，输入网址
        # 第三步，定位
        # 第四步，各种操作
        # 第五步，关闭浏览器
        pass
    def test_d(self):
        # 第一步，打开浏览器
        # 第二步，输入网址
        # 第三步，定位
        # 第四步，各种操作
        # 第五步，关闭浏览器
        pass