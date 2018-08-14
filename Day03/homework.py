__author__ = "Alien"

# 计算器

import re

def add(x,y):
    n = x+y
    return n

def reduce(x,y):
    n = x-y
    return n

def ride(x,y):
    n = x*y
    return n

def chufa(x,y):
    n = x/y
    return n
res = re.search("\(.+\)","2*2+(1+2)+((1+2)-5)")
print(res)


# def Calculator():
#     form = input("输入算数式：")
#     while True:
#         re.search("\(.+\)",form)