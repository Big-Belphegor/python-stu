__author__ = "Alien"

import time

print(time.time())          # 时间戳，以秒为单位
print(time.localtime())     # 打印本地的时间(时区都与本地相同)为时间组

print(time.timezone)        # 时区
a = -28800/3600             # 中国在东八区(UTC-8)，所以是-8.0
print(a)
print(time.gmtime(1820455584))      # 将自定义的时间戳转换为时间组