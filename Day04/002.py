__author__ = "Alien"
# 类的继承

class People(object):
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating" % self.name)

    def sleep(self):
        print("%s is sleeping" % self.name)

class Man(People):
    def run(self):
        print("%s run!" % self.name)

class Woman(People):
    def buy(self):
        print("%s buy!" % self.name)

m1 = People("Alien")
m1.eat()
m1.sleep()

m2 = Man("Jsion")
m2.eat()
m2.sleep()
m2.run()

m3 = Woman("Hy")
m3.eat()
m3.sleep()
m3.buy()