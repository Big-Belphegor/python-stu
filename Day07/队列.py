__author__ = "Alien"
# Queue队列(消息队列)
# 作用：
# 1、解耦
# 2、提高处理效率

import queue

q = queue.Queue()       # 生成对象，默认不限制队列大小
q.put("d1")             # 队列写入数据
q.put("d2")
q.qsize()               # 打印队列大小
print(q.get())          # 获取队列数据，顺序是先入先出，不能根据索引查看
print(q.get())          # 获取队列数据，顺序是先入先出，不能根据索引查看

q.get_nowait()          # 当队列没有可返回的数据时会卡住，用该命令查看

q2 = queue.Queue(maxsize=2)     # 设定队列大小
q2.put('1')
q2.put('1')             # 如果再写入数据就会卡住，除非同一时间有人将数据取出

q3 = queue.LifoQueue()  # 后进先出，让最后写入的数据先被输出
q3.put('1')
q3.put('2')
q3.put('3')
print(q3.get())
print(q3.get())


q4 = queue.PriorityQueue()      # 为数据添加优先级
q4.put((3,'Jsion'))             # 可以用数值排序，也可以是字母排序
q4.put((1,'Alien'))
q4.put((2,'Hy'))
print(q4.get())
print(q4.get())
print(q4.get())