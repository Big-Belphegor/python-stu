__author__ = "Alien"
import time,threading,queue
# 创建一个“生产者”和两个“消费者”，实现通过队列同时对两个用户“服务”。下面是一个小模型，供参考：
q = queue.Queue()

def Boss():
    count = 1
    while True:
        q.put('子弹%s' % count)
        print('生产子弹：',count)
        count += 1
        time.sleep(1)

def Customer(name):
    while True:
        print('[%s] 获取：%s' % (name,q.get()))

b = threading.Thread(target=Boss)
u1 = threading.Thread(target=Customer,args=('Jsion',))
u2 = threading.Thread(target=Customer,args=('Alien',))

b.start()
u1.start()
u2.start()