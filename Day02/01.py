__author__ = "Alien"
# 装饰器，普通版(装饰器不传参数模式)
# import time
#
# def timer(func):
#     def deco():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("The func run time is %s" % (stop_time-start_time))
#     return deco
#
# @timer
# def test1():
#     time.sleep(2)
#     print("This is test1")
#
# test1()

# 装饰器，升级版(根据默认传入参数运行不同"认证")
# user1,passwd1 = 'Alien','123456'
# sshd_key = 'Jsion654321'
#
# def auth(auth_type):
#     def out_wrapper(func):
#             def wrapper(*args, **kwargs):
#                 if auth_type == "userpw":
#                     username = input("Username:")
#                     password = input("Password:")
#                     if username == user1 and password == passwd1:
#                         print("Success in boarding!")
#                         func(*args,**kwargs)
#                     else:
#                         print("Invalid username or password!")
#                 elif auth_type == "sshdkey":
#                     keyname = input("Your key:")
#                     if keyname == sshd_key:
#                         print("Success in boarding!")
#                         func(*args, **kwargs)
#                     else:
#                         print("Invalid username or password!")
#             return wrapper
#     return out_wrapper
#
# @auth(auth_type="userpw")
# def test1():
#     print("This is test1")
#
# @auth(auth_type="sshdkey")
# def test2():
#     print("This is test2")
#
# test1()
# test2()

# 生成器
# def fib(max):
#     n,a,b, = 0,0,1
#     while n < max:
#         yield b
#         a,b = b,a+b
#         n = n +1
# 逐个迭代：
# f=fib(10)
# print(next(f))
# print(f.__next__())

# 循坏迭代：
# while True:
#     try:
#         x = next(g)
#         print('g:',x)
#     except StopAsyncIteration as e:
#         print('Generator return value:',e.value)
#         break

