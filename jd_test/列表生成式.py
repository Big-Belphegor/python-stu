__author__ = "Alien"

# 列表生成式格式
a = [x*2 for x in range(10)]
print(a)

# 在列表生成式内嵌套函数
def test(x):
    return x*x

b = [test(i) for i in range(10)]
print(b)