__author__ = "Alien"

import time,datetime

# print(time.time())                  # 时间戳，以秒为单位
# print(time.localtime())             # 将本地当前时间戳转为时间组
# print(time.gmtime(1820455584))      # 将自定义时间戳转换为时间组
#
# print(time.timezone)                # 时区
# a = -28800/3600                     # 中国在东八区(UTC-8)，所以是-8.0
# print(a)
#
# x = time.localtime()                # 获取时间组中某个值
# print(x)
# print(x.tm_yday)
#
# print(time.mktime(x))               # 将时间组转换为时间戳
#
# print(time.strftime("%y-%m-%d %H:%M:%S"))                       # 将当前时间转为字符串
# print(time.strptime("18-08-10 14:56:30",'%y-%m-%d %H:%M:%S'))   # 将时间字符串转为时间元组

# print(datetime.datetime.now())        # 查看当前时间

import random
# print(random.randint(1,5))              # 随机1-5之间的数
# print(random.randrange(5))              # 随机0-4之间的数
# print(random.choice('hello'))           # 从后面的值中随机打印一个(可以是元组、列表)
# print(random.choice([1,2,3,4]))         # 从后面的值中随机打印一个(可以是元组、列表)
#
# print(random.uniform(1,5))              # 1-5区间内随机打印
#
# tt = [1,2,3,4,5]
# random.shuffle(tt)                      # 打乱原有顺序，每次都不一样(洗牌功能)
# print(tt)

# 小实例：随机打印4个数字
changenum = ''

for i in range(4):
    num1 = random.randrange(0,4)
    if i == num1:
        tmp = chr(random.randint(10,20))    # 转为字母
    else:
        tmp = random.randint(0,9)
    changenum += str(tmp)+' '

print(changenum)