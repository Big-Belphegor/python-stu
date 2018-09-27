__author__ = "Alien"
import re

# 正则符号'.'，只能代指一个字符
r = re.findall('w..l','Hello world')
r2 = re.findall('w.l','Hello world')
print(r)
print(r2)