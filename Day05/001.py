__author__ = "Alien"

# 静态方法
# class test(object):
#     def __init__(self,x):
#         self.x = x
#     @staticmethod       # 让其下方的方法不能调用类的self
#     def fun1(self):     # 添加该静态方法后将self去掉
#         # print('%s is %s' % (self.x,'Teacher'))
#         print('%s is %s' % ('Jsion','Teacher'))

# a = test('Jsion')
# a.fun1()

# b = test('xxx')
# b.fun1(b)


# 类方法
# class test2(object):
#     y = 'a'
#     def __init__(self,y):
#         self.y = y
#
#     @classmethod        # 作用：只能调用同名类变量，不能调用实例变量
#     def fun1(self):
#         print('%s and %s' % (self.y,'B'))
#
#
# c = test2('A')
# c.fun1()

# 属性方法
# class test3(object):
#     def __init__(self,z):
#         self.z = z
#
#     @property     # 作用：把一个方法变成一个静态属性
#     def fun1(self):
#         print('%s and %s' % (self.z,'B'))
#
# d = test3('AAA')
# # d.fun1()        # 加括号会报错
# d.fun1
# 注意：此时的d.fun1默认是不能删除的(del d.fun1)

# 反射
class test4(object):
    def __init__(self,name):
        self.name = name

    def fun1(self):
        print('%s is beauty' % self.name)


e = test4('Hy')
e1 = input('>>').strip()

print(hasattr(e,e1))        # hasattr 判断一个对象‘e’中是否有对应字符串的方法映射

fun2 = getattr(e,e1)        # getattr 根据输入的字符串，去对象'e'中查找对应的方法的内存地址
fun2()                      # 运行匹配到的内存地址