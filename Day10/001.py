__author__ = "Alien"
class test():
    a = 1
    def b(self):
        print('Test')

# def test():
#     a = 1

f1 = test()                 # 将类传进一个变量中
if hasattr(f1,'a'):         # 格式：hasattr(变量,字符串) hasattr作用：判断变量里是否有字符串内的内容，有的话返回True否则False
    func = getattr(f1,'a')  # 格式：getattr(变量,字符串) getattr作用：运行变量里和字符串对等的函数
    print(func)
else:
    print('Error')


# class My_api():
#     def __init__(self,obj,*args,**kwargs):
#         self.obj = obj
#         self.args = args
#         self.kwargs = kwargs
#
#     def get(self,*args,**kwargs):
#         t1 = test()
#         if hasattr(t1,self.obj):
#             inside_obj = getattr(t1,self.obj)
#             put_obj = inside_obj(self.args,self.kwargs)
#             return put_obj
#         else:
#             return 'Error'
#
# a = My_api('a','Json')
# print(a.get())