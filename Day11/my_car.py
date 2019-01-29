__author__ = "Alien"
'''实际工作中通常将一部分类创建独立的模块，这样就不会显得代码太长'''

# import sys
# print(sys.path)
# sys.path.append("F:\\python-stu\\Day10")

from car import Car
from Day10.cc import My_api

t1 = My_api(1)
t1.test()
# my_new_car = Car('Audi','R8','2019')
# print(my_new_car.read_odometer())