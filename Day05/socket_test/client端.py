__author__ = "Alien"
# 客户端
import socket

client = socket.socket()                # 声明socket类型，同时生成socket连接对象
client.connect(('localhost',8080))      # 连接Server端口

client.send(b'Hello world')             # 发送数据给Server，注意：python3后数据必须是二进制
data = client.recv(1024)                # 接受数据，大小设置为1024字节
print("recv:",data)                     # 打印收到的数据

client.close()