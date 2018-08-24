__author__ = "Alien"
#服务端

import socket
server = socket.socket()

server.bind(('localhost',8080))     # 设置监听端口
server.listen()                     # 开始监听端口
print('电话连接中...')

conn,addr = server.accept()         # 双方端口连接成功
print('182xxxx8888来电了')

data = conn.recv(1024)              # 接受连接数据，设置大小为1024字节
print('recv:',data)                 # 打印接受到的数据
print('recv:',data.decode())        # 也可以打印中文，但需要转码
conn.send(data.upper())             # 将接受到的数据改为大写，重新发送给出去

server.close()