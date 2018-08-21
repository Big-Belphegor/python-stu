__author__ = "Alien"

class test:
    n = 123 # 类变量
    def __init__(self,name,sex,age):
        # 构造函数
        self.name = name        # 实例变量
        self.sex = sex
        self.age = age

    def profile(self):
        print('''
            Your name: %s
            Your sex: %s
            Your age: %s
        ''' % (self.name,self.sex,self.age))

print(test)
a = test('Alien','M','24')
a.profile()
print(test.n)