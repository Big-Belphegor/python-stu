__author__ = "Alien"
# 异常处理（对即将出现的错误做出预判，简单说就是将预期内的错误改成自己想要的返回模式）
# 比如：列表a没有第三个索引，当用户查找第三个索引时，不要系统报错，而是自定义的错误提示。

# 格式:
#     try:
#     --有可能出现问题的代码段
#     except 错误类型 as e:
#     --执行遇到该类型错误后执行的内容

# 实例：
# a = [1,2]
# b = {}
#
# try:
#     a[3]
#     b['haha']
#
# except IndexError as e:
#     print('Index不存在')
#
# except KeyError as e:
#     print('Key不存在')
#
# except Exception as e:                # 不管什么错误都接直接except
#     print('出错了，具体是啥不知道')
# except (IndexError,KeyError) as e:    # 可以处理多个错误
#     print('没有key也没有index')