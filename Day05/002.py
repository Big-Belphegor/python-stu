__author__ = "Alien"
# 异常处理（对即将出现的错误做出预判，简单说就是将预期内的错误改成自己想要的返回模式）
# 比如：列表a没有第三个索引，当用户查找第三个索引时，不要系统报错，而是自定义的错误提示。

# 格式:
#     try:
#     --有可能出现问题的代码段
#     except 错误类型 as e:
#     --执行遇到该类型错误后执行的内容
#     else:
#     --否则就是没有错误



# 实例：
# a = [1,2]
# b = {}

# try:
    # a[3]
    # b['haha']
#     a[2]
#
# except IndexError as e:
#     print('Index不存在',e)

# except KeyError as e:
#     print('Key不存在',e)
#
# except (IndexError,KeyError) as e:    # 可以处理多个错误
#     print('没有key也没有index',e)
#
# except Exception as e:                # 抓位置错误
#     print('出错了，具体是啥不知道',e)

# else:
#     print('一切正常')
#
# finally:                                # 不论是否出错，都会运行
#     print('谁都不能阻止我运行')
#
# 自定义异常
class DIYError(Exception):
    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message
try:
    raise DIYError('自定义的异常')
except DIYError as e:
    print(e)




