

# 可以使用from  import * 来使用这个函数
# 表示 需要暴露给外界的变量，函数，已经类，是一个借口
# 只要写在列表里的内容才会暴露给外界，不然是不会暴露给外界
# __all__ = ['hello']


hello = "hello python"

def f():
    print("hello python")


class demo2():
    pass