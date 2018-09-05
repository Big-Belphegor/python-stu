__author__ = "Alien"
import threading,time

# 实例化 实现多线程实例：
# def run(n):
#     print('Cli,Cli',n)
#     time.sleep(2)
#
# t1 = threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run,args=("t2",))
# # 一共用时2s
# t1.start()
# t2.start()
# # 一共用时4s
# run(1)
# run(2)


# 类 实现多线程实例(有些麻烦，可以使用上面的写法):
# class MyThread(threading.Thread):
#     def __init__(self,n):
#         super(MyThread,self).__init__()
#         self.n = n
#
#     def run(self):
#         print('running task',self.n)
#
# t1 = MyThread('t1')
# t2 = MyThread('t2')
#
# print(t1.run())
# print(t2.run())

# 创建多个子线程(介绍join方法)
# start_time = time.time()
# t_obj = []
# def run(n):
#     print(n)
#     time.sleep(2)
#
# for i in range(50):
#     t = threading.Thread(target=run,args=('t-%s' % i,))
#     t.start()
#     t_obj.append(t)     # 将启动的线程写入到一个列表里，为了不影响下一个要启动的线程
# print('当前活动线程个数:%s' % threading.active_count())
#
# for x in t_obj:
#     x.join()            # 功能：让主线程等待子线程执行完毕后再运行，目的就是让所有的线程都执行结束后在结束主线程
#
# #注意：程序本身就会占用一个线程，这个线程称之为主线程。所以本实例，其实是并行这运行了51个线程。
# print('程序共费时:%s 当前活动线程个数:%s' % (time.time()-start_time,threading.active_count()))


# 创建守护线程，将子线程转化为守护线程。
# 效果：主线程不会关心子线程(守护线程)是否运行完毕，只会等待父线程(非守护线程)结束后直接结束。
# start_time = time.time()
# t_obj = []
# def run(n):
#     print(n)
#     time.sleep(2)
#     print('%s Done' % n)
#
# for i in range(50):
#     t = threading.Thread(target=run,args=('t-%s' % i,))
#     t.setDaemon(True)         # 将当前线程变成守护线程,注意：一定要在start之前
#     t.start()
#     t_obj.append(t)
# print('当前活动线程个数:%s' % threading.active_count())
# print('程序共费时:%s 当前活动线程个数:%s' % (time.time()-start_time,threading.active_count()))

# 线程锁
# 作用：在锁内的线程是独立的，其它线程不能干扰。
# def run(n):
#     lock.acquire()          # 添加锁
#     global num              # (实际中此处可以是一些能够快速运算并得出结果的代码)
#     num += 1
#     time.sleep(1)
#     lock.release()          # 释放锁
#
# lock = threading.Lock()     # 创建锁
# num = 0
# t_objs = []
# for i in range(10):
#     t = threading.Thread(target=run,args=('t-%s' % i,))
#     t.start()
#     t_objs.append(t)
#
# for t in t_objs:
#     t.join()
#
# print('Over',threading.current_thread())
# print('Num:',num)


# 线程递归锁
def run():
    locks.acquire()
    global num
    num += 1
    locks.release()
    return num

def run2():
    locks.acquire()
    global num2
    num2 += 1
    locks.release()
    return num2

def run3():
    locks.acquire()
    print('run1:',run())

    print('run2:',run2())

    locks.release()

num,num2 = 0,0
locks= threading.RLock()                # 创建递归锁
for i in range(1):
    t = threading.Thread(target=run3)
    t.start()

while threading.active_count() != 1:
    pass
else:
    print('-----Over-----')
    print(num,num2)