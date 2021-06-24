import pytest
import yaml

from web.selenium_TCLAD.page.main import Main


class Test_AD:
    # def setup(self):
    #     self.ad = Main()
    #
    # def teardown(self):
    #     self.ad.quit()

    def setup_class(self):
        self.ad = Main()
    def teardown_class(self):
        self.ad.quit()

    @pytest.mark.parametrize("clite_type",yaml.safe_load(open('../test_date/date.yaml')))
    def test_add_resource(self,clite_type):
        self.ad.goto_launcher().goto_resource_management().add_resource()
        self.ad.goto_launcher().goto_system_managment()


        #self.ad 调用login() 进入到goto_launcher()点击资源管理进入到goto_resource_management()，在里面获取列表结果
        assert self.ad.goto_launcher().goto_resource_management().get_resource(clite_type)

    @pytest.mark.skip
    def test_system(self):
        self.ad.goto_launcher().goto_system_managment()
