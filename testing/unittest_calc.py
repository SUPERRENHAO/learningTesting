import unittest
import sys

# print(sys.path)
sys.path.append("..")
from python.calc import calc

# 如果需要使用python自带的环境去运行的话，需要在带入这个框架前倒入一下路径
# sys.path python的工作环境的话，pycharm会先在sys.path这个路径去找你需要倒入的包，但如果使用python命令行去执行的话就会报错
# 我们可以手动添加路径在解决这个问题

class TestClac(unittest.TestCase):

    def test_add(self):
        self.calc = calc()

        print(self.calc.add(3,5))
        self.assertEqual(8,self.calc.add(3,5))


# 在units需要在命令调用的时候，就需要加上这个东西
if __name__ == '__main__':
    unittest.main()
