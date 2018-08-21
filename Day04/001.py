__author__ = "Alien"

class test:
    n = 123 # 类变量
    def __init__(self,name,sex,age,n):
        # 构造函数
        self.name = name        # 实例变量(实例变量的作用域就是实例本身)
        self.sex = sex
        self.age = age
        self.n = n

    def profile(self):          # 类的方法，功能
        print('''
            Your name: %s
            Your sex: %s
            Your age: %s
            Other n: %s
        ''' % (self.name,self.sex,self.age,self.n))

print(test)

a = test('Alien','M','24','f')      # 实例化
a.profile()
print(a.n)
print(test.n)

