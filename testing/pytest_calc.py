import pytest

from python.calc import calc



class Test_calc():
    def setup(self):
        self.calc = calc()

    def test_add(self):
        # self.calc = calc()
        # self.calc.add(.)
        result = self.calc.add(3,5)
        print(result)
        assert 8 == result

    def test_div(self):
        # self.calc = calc()
        result = self.calc.div(4,2)
        print(result)
        assert  2 == result


if __name__ == '__main__':
    pytest.main(['-vs','pytest_calc.py::Test_calc::test_div'])
