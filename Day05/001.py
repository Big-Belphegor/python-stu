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

# 反射 （完成用户输入的字符串判断及调用对应的函数）
# 部分一(hasattr 和 getattr)
# class test4(object):
#     def __init__(self,name):
#         self.name = name
#
#     def fun1(self):
#         print('%s is beauty' % self.name)
#
#
# e = test4('Hy')
# f = input('>>').strip()
#
# if hasattr(e,f):               # hasattr 判断一个对象‘e’中是否有对应'e1'变量中的字符串的方法映射，格式：hasattr(obj,str)
#     a = getattr(e,f)           # getattr 根据输入的字符串，去对象'e'中查找对应的方法的内存地址,格式：getattr(obj,str)
#     a()                        # 运行匹配到的内存地址
# else:
#     print('Not found!')

# 部分二(setattr使用模式一)
# class test4(object):
#     def __init__(self,name):
#         self.name = name
#
#     def fun1(self):
#         print('%s is beauty' % self.name)
#
#
# e = test4('Hy')
# f = input('>>').strip()
#
# if hasattr(e,f):               # hasattr 判断一个对象‘e’中是否有对应'e1'变量中的字符串的方法映射，格式：hasattr(obj,str)
#     a = getattr(e,f)           # getattr 根据输入的字符串，去对象'e'中查找对应的方法的内存地址,格式：getattr(obj,str)
#     a()                        # 运行匹配到的内存地址
# else:
#     setattr(e,f,None)          # 如果输入的字符串不存在类中，就自行创建一个函数。格式：setattr(obj,str,fun)
#     b = getattr(e,f)
#     print(b)

# 部分三(setattr使用模式二 和 delattr)
def fun2(self):
    print('This is fun2:',self.name)

def fun3(x):
    print('This is fun3:',x)

class test5(object):
    def __init__(self,name):
        self.name = name

    def fun1(self):
        print('This is fun1:',self.name)

a = test5('Jsion')
b = input('>>').strip()

if hasattr(a,b):
    delattr(a,b)            # 删除一个attr此时再运行程序输入fun1回车会报错(提示找不到这个函数)，格式：delattr(obj,str)
else:
    # setattr(a,b,fun2)       # 通过字符串的形式，将类外的方法映射到‘类里’,格式：setattr(obj,str,fun)
    # fun2(a)
    setattr(a,b,fun3)       # 注意：此处是重新传进了一个新的函数fun3
    c = getattr(a,b)        # 此时的c等于附上了函数fun3
    c(b)

