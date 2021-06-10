import pytest
import yaml

from python.calc import calc
from testing.conftest import *


def err_to_AB(a,b):
    print(a,b)
    if b == 0 :
        raise NameError("分母不能为0")
    pass
# def err_to_string(a,b):
#     if isinstance(a,str) | isinstance(b,str) :
#         raise NameError("不能含有字符型")
#         pass
# def err_to_null(a,b):
#     if not a|b is None:
#         pass
#     else:
#         raise NameError("不能为空")

class Test_calc():
    def setup(self):
        self.calc = calc()
        self.a = 5
        self.b = 0

    @pytest.mark.parametrize("a,b,results",yaml.load(open("./testDate.yml"),Loader=yaml.FullLoader))
    def test_add(self,a,b,results):

        result = self.calc.add(a,b)

        relese_result = results["reslut"][0]["add"]
        print(result)
        # err_to_fenmu(self.a,self.b)

        assert result == relese_result

    def test_jian(self):
        # pass
        result = self.calc.jian(self.a,self.b)
        assert 4 == result

    def test_cheng(self):
        result = self.calc.cheng(self.a,self.b)
        assert 10 == result

    def test_div(self):
        # self.calc = calc()
        a,b=3,0
        result = self.calc.div(a,b)
        # err_to_fenmu(a,b)

        print(result)
        assert  2 == result


if __name__ == '__main__':
    pytest.main(['-vs','pytest_calc.py::Test_calc::test_add'])
