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


# 创建守护线程，就是将子线程转化为守护线程
start_time = time.time()
t_obj = []
def run(n):
    print(n)
    time.sleep(2)
    print('%s Done' % n)

for i in range(50):
    t = threading.Thread(target=run,args=('t-%s' % i,))
    # t.setDaemon(True)         # 将当前线程变成守护线程，可已通过注释/解注释该行进行测试
    t.start()
    t_obj.append(t)
print('当前活动线程个数:%s' % threading.active_count())
print('程序共费时:%s 当前活动线程个数:%s' % (time.time()-start_time,threading.active_count()))
# 注意： 当子线程变成守护线程时，主线程不会等待其是否运行结束；反之，主线程会默认在执行结束后添加join功能等待所有线程结束后在退出程序。