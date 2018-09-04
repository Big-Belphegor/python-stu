__author__ = "Alien"
# 进程地址池
from multiprocessing import Pool
import time,os

def Foo(i):
    time.sleep(2)
    print('In process',os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__ == '__main__':          # 手动执行时，只有是在本文件是才会执行下面的程序
    pool = Pool(3)                  # 运行进程池里同时存在5个进程
    print("主进程：",os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)     # callback作用：回调；等func运行结束后再运行callback
        # pool.apply(func=Foo, args=(i,))           # apply是串行
        # pool.apply_async(func=Foo, args=(i,))     # apply_async是并行

    print('end')
    pool.close()
    pool.join()                     # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭