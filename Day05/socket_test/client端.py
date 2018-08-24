__author__ = "Alien"
# 客户端
import socket

client = socket.socket()                # 声明socket类型，同时生成socket连接对象
client.connect(('localhost',8080))      # 连接端口

client.send(b'Hello world')             # 要发送的数据
data = client.recv(1024)                # 接受数据，大小设置为1024字节
print("recv:",data)                     # 打印收到的数据

client.close()