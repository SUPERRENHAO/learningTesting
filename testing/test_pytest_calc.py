import pytest
import yaml
# import traceback
from python.calc import calc
from testing.conftest import *
# 涉及精度的时候使用这个
from decimal import Decimal
# 设置Decimal精度问题
from decimal import getcontext

getcontext().prec = 1

# def err_to_AB(a,b,mark):
#
#     # print("‘%s Invoked me!’%s"[-2][2])
#     if mark == "div" and b == 0:
#         raise NameError("分母不能为0")
#     elif a == '' or b == '':
#         raise NameError("他们的参数不能为空")
#     elif isinstance(a,str) | isinstance(b,str) :
#         raise NameError("参数不能为字符型")
    # print(a,b)
    # if b == 0 :
    #     raise NameError("分母不能为0")
    # pass

# 设置打开文件

def steps():
    with open("./datas/steps.yml") as f:
        return  yaml.safe_load(f)

class Test_calc():
    # 预置条件
    def setup(self):
        self.calc = calc()

    #打标签
    # @pytest.mark.add
    # 设置执行顺序
    # @pytest.mark.run(oreder=2)
    #参数化传递yaml的值
    @pytest.mark.parametrize("a,b,results",yaml.load(open("./testDate.yml"),Loader=yaml.FullLoader))
    def test_add(self,a,b,results):
        print("add")
        #在使用ab之前需要进行一个异常处理
        # err_to_AB(a,b,mark)
        # 获取实际结果
        result = self.calc.add(Decimal(a),Decimal(b))
        # 获取预期结果
        relese_result = results["reslut"]["add"]
        print(result)
        # err_to_fenmu(self.a,self.b)

        assert Decimal(relese_result) == result

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,results", yaml.load(open("./testDate.yml"), Loader=yaml.FullLoader))
    def test_add1(self, a, b, results):
        # 测试步骤数据驱动
        steps1 = steps()
        print(steps1)
        # 通过这个测试步骤数据驱动来进行
        for step in steps1:
            print(f"step =====>  {step}")
            if 'add' == step:
                result = self.calc.add(a,b)
            elif 'add1' == step:
                result = self.calc.add1(a,b)
        print(result)
        relese_result = results["reslut"]["add"]

        assert relese_result == result

        # print("add1")
        # # 在使用ab之前需要进行一个异常处理
        # # err_to_AB(a,b,mark)
        # # 获取实际结果
        # print(Decimal(a))
        # print(Decimal(b))
        # print(Decimal(self.calc.add(a, b)))
        # result = self.calc.add(a,b)
        # # result1 = Decimal(result).quantize(Decimal("0.0"))
        # # 获取预期结果
        # relese_result = results["reslut"]["add"]
        #
        # print(result)
        # # err_to_fenmu(self.a,self.b)
        # #Decimal(relese_result).quantize(Decimal('0.000')) == result
        #
        # assert relese_result == result

    # def test_jian(self):
    #
    #     # pass
    #     result = self.calc.jian(self.a,self.b)
    #     assert 4 == result
    #
    # def test_cheng(self):
    #     result = self.calc.cheng(self.a,self.b)
    #     assert 10 == result
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,results", yaml.load(open("./testDate.yml"), Loader=yaml.FullLoader))
    def test_div(self,a,b,results):
        print("div")
        result = self.calc.div(Decimal(a),Decimal(b))
        #["reslut"][0]["add"]
        print(a,b,results["reslut"]["div"])
        # err_to_fenmu(a,b)
        relesr_result = results["reslut"]["div"]

        print(result)
        assert  Decimal(relesr_result) == result


# if __name__ == '__main__':
#     pytest.main(['-vs','test_pytest_calc.py::Test_calc::test_div'])
