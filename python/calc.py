#  type hints 类型提示
import traceback

# 异常处理
def err_to_AB(a,b,mark):

    # print("‘%s Invoked me!’%s"[-2][2])
    try:
        if ( b == 0 and mark == "div"):
            raise ZeroDivisionError("除数不能为0")

    except ValueError as e:
        print("引发异常",repr(e))



class calc():
    func_list = []

    def add(self, a: int, b: int) -> int:


        return a + b

    def add1(self, a: int, b: int) -> int:

        return a + b

    def div(self, a: int, b: int):
        mark = "div"
        err_to_AB(a, b, mark)
        return a / b

    def jian(self, a: int, b: int):
        mark = "jian"
        err_to_AB(a, b, mark)
        return a - b

    def cheng(self, a: int, b: int):
        mark = "cheng"
        err_to_AB(a, b, mark)
        return a * b
