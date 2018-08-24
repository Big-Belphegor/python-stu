__author__ = "Alien"
#服务端

import socket
server = socket.socket()

server.bind(('localhost',8686))     # 绑定要监听端口
server.listen()     # 监听端口

print('电话连接中...')
conn,addr = server.accept()     # 等电话
print(conn,addr)

print('182xxxx88968来电了')
data = conn.recv(1024)
print('recv:',data)
conn.send(data.upper())

server.close()