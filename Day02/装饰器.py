__author__ = "Alien"
import time

# 基础部分
# def showtime(f):
#     def t1():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#
#         print('程序用时：',end_time-start_time)
#     return t1
#
# @showtime             # 此处就等于 add=showtime(add)
# def add():
#     time.sleep(2)
#     print('Over!')
#
# add()

# 中级部分(被装饰函数传入参数)
# def show_time(f):
#     def t2(*args,**kwargs):
#         start_time = time.time()
#         f(*args,**kwargs)
#         end_time = time.time()
#         print('程序用时：',end_time - start_time)
#
#     return t2
#
# @show_time
# def add2(*args,**kwargs):            # 配置位置参数
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#     time.sleep(1)
#
# add2(1,2)

# 高级部分(装饰器传入参数)
def logger(a):
    def show(b):
        def t3(*args,**kwargs):
            start_time = time.time()
            b(*args,**kwargs)
            end_time = time.time()
            print('程序用时：',end_time - start_time)
            if a == 'T':
                print('This is a log')
            else:
                pass
        return t3
    return show


@logger('T')                        # 传入一个预先定义好的参数，有T的参数就写入日志
def add3(*args,**kwargs):
    sum = 0
    for i in args:
        sum += i
    print(sum)
    time.sleep(1)

@logger('F')                        # 没有这个参数就不输入到日志
def add4(*args,**kwargs):
    sum = 0
    for i in args:
        sum += i
    print(sum)
    time.sleep(1)

add3 (1,2)
add4(2,2)