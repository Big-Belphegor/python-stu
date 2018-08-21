__author__ = "Alien"
# 类的继承

class People(object):           # 父类
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating" % self.name)

    def sleep(self):
        print("%s is sleeping" % self.name)

class Man(People):              # 子类(继承的People）
    def run(self):
        print("%s run!" % self.name)

class Woman(People):            # 子类(继承的People）
    def buy(self):
        print("%s buy!" % self.name)

class xxx(People):              # 给子类单独添加属性
    def __init__(self,name,xxxfun):
        # 方法一
        # People.__init__(self,name)
        # self.xxxfun = xxxfun
        # 方法二(优于方法一)
        super(xxx,self).__init__(name)
        self.xxxfun = xxxfun

    def testfun(self):
        print("%s 用户获得特殊属性：%s" % (self.name,self.xxxfun))


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

m4 = xxx("Tom","遁地术")
m4.eat()
m4.sleep()
m4.testfun()
# 注意：类Man和类Woman不发生任何关系，但是它们都可以同时继承People类下的方法