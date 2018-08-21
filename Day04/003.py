__author__ = "Alien"
# 类的多继承
class Af:                           # 父类1
    def __init__(self,name):
        self.name = name

    def whoami(self):
        print("My name is %s" % self.name)

class Bf(object):                   # 父类2
    def wtf(self,obj):              # 没有构造函数，子类会到另外的父类寻找，如父类1中的self.name
        print("%s is an special %s" % (self.name,obj))  # 因此，此处没有直接报错。

class Cu(Af,Bf):                    # 子类1
    def one(self):
        print("This is Cu")

class Du(Af,Bf):                    # 子类2
    def two(self):
        print("This is Du")

a = Cu('Alien')
a.wtf('fun')