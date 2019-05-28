__author__ = "Alien"
import time
# 装饰器实例

# 被装饰函数有传入参数
def show_time(func):
    def inside(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print('Speed is %s' % (end - start))
    return inside

@show_time
def login_test(x):
    print('Your name %s' % x)
    time.sleep(1)

login_test('Alien')

# 被装饰函数无传入参数
def insert_func(func):
    def main():
        func()
        print('======= %s =======' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return main

@insert_func
def Logout():
    print('Looking forward to your next visit.')

Logout()