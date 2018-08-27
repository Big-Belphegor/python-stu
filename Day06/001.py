__author__ = "Alien"
import importlib        # 动态导入模块

a = importlib.import_module('test-module.test-1')       # 直接将test-1模块导入
print(a)
print(a.tt().name)
assert type(a.tt().name) is int     # 断言，用于判断前半部分返回值是否为后面的属性，格式：assert ... is ...
assert type(a.tt().name) is str     # 如果出现，前后不匹配，直接报错打断程序运行
