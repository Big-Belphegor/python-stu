__author__ = "Alien"

# 新式类与经典类区别：类的继承顺序不同

# 继承策略1：广度优先 (D找不到构造函数后，首先到B类查找，如果没有再去C类查找，还是没有就去A类查找)
class A:
    def __init__(self):
        print("A")

class B(A):
    pass
    # def __init__(self):
    #     print("B")

class C(A):
    pass
    # def __init__(self):
    #     print("C")

class D(B,C):
    pass

print(D())

# 继承策略2：深度优先 (D找不到构造函数后，首先到B类查找，但是由于B类也继承了A类，所以再次寻找会去A类寻找，A类没有再去C类查找)
#（python2 会自动使用这个，Python3自动使用）
class A:
    def __init__(self):
        print("A")

class B(A):
    pass
    # def __init__(self):
    #     print("B")

class C(A):
    pass
    # def __init__(self):
    #     print("C")

class D(B,C):
    pass

print(D())