import pytest

from web.selenium_wework.wework_main.page.main import Main


class Test_addMember:
    def setup(self):
        self.wework = Main()


    # @pytest.mark.skip
    def test_addMember(self):
        self.wework.goto_tongxunle().goto_addMember().add_member()
        assert self.wework.goto_tongxunle().goto_addMember().get_member('9atest_case1')

    @pytest.mark.skip
    def test_demo(self):
        str = '1/9'
        con,con2 = [int(x) for x in str.split('/',1)]
        print('con',con)
        print('con2',con2)
        print(str.split('/', 1))
        print(type(str[0]))
