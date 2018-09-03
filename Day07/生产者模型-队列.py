__author__ = "Alien"
import time,threading,queue

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