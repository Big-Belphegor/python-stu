__author__ = "Alien"
# 客户端
import socket

client = socket.socket()                # 声明socket类型，同时生成socket连接对象
client.connect(('localhost',8080))      # 连接Server端口

# client.send('我是Jsion'.encode('utf-8'))    # 可以发送中文，需要转码
client.send(b'Hello world')             # 发送数据给Server，注意：python3后数据必须是二进制；不能send空
data = client.recv(1024)                # 接受数据，大小设置为1024字节，官方建议最大不要超过8192字节
print("recv:",data)                     # 打印收到的数据
# print("recv:",data.decode())            # 打印中文，需转码

client.close()