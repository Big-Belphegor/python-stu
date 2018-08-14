__author__ = "Alien"

# 计算器

import re

def add(x,y):
    return x+y

def reduce(x,y):
    return x-y

def ride(x,y):
    return x*y

def chufa(x,y):
    return x/y

def Calculator():
    form = input("输入算数式：")
    while True:
        re.search("\(.+\)",form)