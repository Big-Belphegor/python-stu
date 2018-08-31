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
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print('running task',self.n)

t1 = MyThread('t1')
t2 = MyThread('t2')

print(t1.run())
print(t2.run())