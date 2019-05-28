__author__ = "Alien"

# # 生成器，其功能就是将可能出现的数据在调用时按照预期进行迭代生成
# # 说白了，下面s参数的值，只有在运行next时才会生成
# s = (x for x in range(10))      # 设定10个值进行生成
#
# for i in s:                     # 获取所有10个值
#     print(i)
#
# print(next(s))                  # 会报错，因为上面代码已经取出全部值

# # 斐波那契数列
# def fbnq(max):
#     n,once,second = 0,0,1
#     while n<max:
#         print(second)
#         once,second = second,once+second
#         n = n+1
# fbnq(10)

def test1():
    print('Frist')
    count = yield 1
    print(count)
    yield 2

t = test1()
next(t)
t.send('New message')

