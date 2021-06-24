
# yield + 函数  == 生成器

def provider():
    for i  in  range(5):
        print("before")
        yield i # 生成器 ： return i  + 暂停此位置，下一次使用next 方法调用的时候，会从当前位置继续往下
        print("after")

p = provider()
print(next(p))
# 会打印before--打印i的值===0

print(next(p))
# 会从上一次断点位置继续往下，
# 先打印after
# 在打印before
# 在打印 i的值====1

print(next(p))
# 会从上一次断点位置继续往下，
# 先打印after
# 在打印before
# 在打印 i的值====2


# 每次打印都是0
# print(provider())
# print(provider())
# print(provider())