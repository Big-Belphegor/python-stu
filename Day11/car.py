__author__ = "Alien"

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0               # 设定默认值，此属性不需要再上面特殊定义

    def read_odometer(self):
        print('This car has ' + str(self.odometer) + ' miles on it')
        return ''

    def update_odometer(self,mileage):  # 通过方法修改属性
        self.odometer = mileage

    def other_function(self):
        pass