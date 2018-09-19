__author__ = "Alien"
import datetime,subprocess,re,time
f = open('logpath','w')
f.close()

ips = ['baidu.com']                 # IP地址池

# def Ipadd():
#     # 自定义添加IP
#     ip = input('Your IP:')
#     ips.append(ip)

def Logadd(func):
    # 添加日志
    def t1():
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')   # 创建时间戳
        f = open('logpath','a')
        a = func()
        f.write('\n%s \n %s' % (str(now_time),a))
        f.close()
    return t1

@Logadd
def Pingip():
    for i in ips:
        p = subprocess.Popen(['C:\Windows\System32\PING.exe',i],        # Ping指定IP
                             stdin=subprocess.PIPE,                     # 标准输入
                             stdout=subprocess.PIPE,                    # 标准输出
                             stderr=subprocess.PIPE,                    # 标准错误
                             shell=True
                             )
        out = p.stdout.read()       # 获取输出
        out = out.decode('gbk')     # 转码

        # 丢包率
        regex = re.compile(r'\w*%\w*')
        packetLossRateList = regex.findall(out)
        packetLossRate = packetLossRateList[0]

        # 往返时间
        regex = re.compile(r'\w*ms')
        timeList = regex.findall(out)
        minTime = timeList[-3]
        maxTime = timeList[-2]
        averageTime = timeList[-1]

        # 打印结果
        reply = {'packetLossRate':packetLossRate,'minTime':minTime,'maxTime':maxTime,'averageTime':averageTime}
        # print(reply)
        return reply

# 运行程序
while True:
    Pingip()
    time.sleep(3)