__author__ = "Alien"
import socket,os
server = socket.socket()            # 生成socket实例

server.bind(('localhost',6666))     # 配置监听IP及端口
server.listen()                     # 开始监听

while True:
    conn,addr = server.accept()     # 等待连接(堵塞)
    print('IP address:',addr)

    while True:
        print('Client connection...')
        data = conn.recv(1024)      # 配置接受数据大小，并赋值给data
        if not data:
            print('Client disconnect!')
            break
        cmd_res = os.popen(data.decode()).read()        # 接受字符串命令，返回结果也是字符串
        print('Total transmission:',len(cmd_res))       # 打印返回结果的大小
        if len(cmd_res) == 0:
            cmd_res = "Not Output!"
        # 下面的操作容易发生粘包
        # conn.send(str(len(cmd_res.encode())).encode('utf-8'))   # 发送命令返回的数据总大小
        # conn.send(cmd_res.encode('utf-8'))                      # 发送命令返回的数据给client端
        # 解决方法两种：
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))
        # time.sleep(0.5)                                         # 最简单粗暴，但并没有太多实际意义
        client_sleep = conn.recv(1024)                            # 做一次接受，这样会自动断开下次的发送
        conn.send(cmd_res.encode('utf-8'))
        print('Over')

server.close()                      # 关闭连接
