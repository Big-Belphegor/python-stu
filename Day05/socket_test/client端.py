__author__ = "Alien"
# 客户端
import socket
client = socket.socket()            # 声明socket类型，同时生成socket连接对象

client.connect(('localhost',8686))
client.send(b'Hello world')
data = client.recv(1024)
print("recv:",data)

client.close()