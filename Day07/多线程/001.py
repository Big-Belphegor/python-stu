__author__ = "Alien"
import threading,time

# 简单的多线程示例：
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


# 用类实现多线程（有些麻烦，可以使用上面的写法）
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

# 测试多线程性能,测试50个线程需要多久运行完
start_time = time.time()
t_obj = []
def run(n):
    print(n)
    time.sleep(2)

for i in range(50):
    t = threading.Thread(target=run,args=('t-%s' % i,))
    t.start()
    t_obj.append(t)
print('当前活动线程个数:%s' % threading.active_count())

for x in t_obj:
    x.join()            # 功能：让主线程等待子线程执行完毕后再运行

#注意：程序本身就会占用一个线程，这个线程称之为主线程。所以本实例，其实是并行这运行了51个线程。
print('程序共费时:%s 当前活动线程个数:%s' % (time.time()-start_time,threading.active_count()))

