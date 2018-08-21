__author__ = "Alien"
# 类的基础知识
class test:     # 经典类定义方式
    n = 123 # 类变量
    def __init__(self,name,sex,age,n,secret):
        # 构造函数
        self.name = name        # 实例变量(实例变量的作用域就是实例本身)
        self.sex = sex
        self.age = age
        self.n = n
        self.__secret = secret  # 私有属性

    def profile(self):          # 类的方法，功能
        print('''
            Your name: %s
            Your sex: %s
            Your age: %s
            Other n: %s
        ''' % (self.name,self.sex,self.age,self.n))

    def __secretfun(self):      # 私有方法，只能内部使用的类功能
        print("外部看不到的变量 %s 和 方法" % self.__secret)

    def __del__(self):
        # 析构函数(在实例释放、销毁的时候执行。如：关闭临时文件等)
        print("\nOver")

print(test)

a = test('Alien','M','24','f','000')      # 实例化
a.profile()

print(a.n)
print(test.n)

