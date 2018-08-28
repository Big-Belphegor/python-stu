__author__ = "Alien"
import socket
client = socket.socket()

client.connect(('localhost',6666))      # 连接server端开放端口

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0: continue          # 输入命令
    client.send(cmd.encode('utf-8'))    # 发送命令给server端
    cmd_res_size = client.recv(1024)    # 接受数据总大小
    print('Total transmission:',cmd_res_size)
    client.send(b"That's ok")           # 用来解决粘包现象，发送任意一段数据来断开连续的send
    received_size = 0                   # 定义接受一次数据的大小(用于计算接受到的数据大小)
    received_data = b''                 # 定义接受数据内容(用于将server端发送的数据转为Binay)
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)        # 将一次循环的数据赋到data中
        received_size += len(data)
        received_data += data
    else:
        print('Transferred size:',received_size)        # 打印已接收的数据大小
        print(received_data.decode())                   # 打印接受到的数据信息

client.close()                          # 关闭连接

