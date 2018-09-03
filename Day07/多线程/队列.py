__author__ = "Alien"
# Queue队列(消息队列)
import queue

q = queue.Queue()       # 生成对象，默认不限制队列大小
q.put("d1")             # 队列写入数据
q.put("d2")
q.qsize()               # 查看队列大小
print(q.get())          # 获取队列数据，顺序是先入先出，不能根据索引查看

q.get_nowait()          # 当队列没有可返回的数据时会卡住，用该命令查看

q2 = queue.Queue(maxsize=2) # 设定队列大小
q2.put('1')
q2.put('1')
q2.put('2')             # 如果再写入数据就会卡住，除非同一时间有人将数据取出

