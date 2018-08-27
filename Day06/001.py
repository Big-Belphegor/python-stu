__author__ = "Alien"
import importlib        # 动态导入模块

a = importlib.import_module('test-module.test-1')       # 直接将test-1模块导入
print(a)
print(a.tt().name)