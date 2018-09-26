__author__ = "Alien"
import configparser

# Python内置的用于写配置文件的模块，效果可以看nginx.conf文件

# 生成一个配置文件
# f = configparser.ConfigParser()
#
# f["DEFAULT"] = {
#     'Name':'Lee',
#     'Sex':'M'
# }
#
# f["Data"] = {
#     'Listen':'80',
#     'server_name':'test.com'
# }
#
#
# with open('nginx.conf','w') as d:
#     f.write(d)


# 读取一个配置文件
# f2 = configparser.ConfigParser()
# f2.read('nginx.conf')
# a = f2.sections()       # 查看所有字节，不包含default
# b = f2.defaults()       # 用于查看default部分
# print(a)
# print(b)
#
# for x in f2['Data']:    # 循环打印，注意：default也会跟着被打印出来
#     print(x)

# 删除配置文件中的某项
# f2.remove_section('Data')

# 改写
# f2.remove_section('Data')
# f2.write(open('nginx.conf.bak','w'))

# 判断字段是否出现在配置文件中
# s = f2.has_section('Data')
# print(s)

# 修改
f3 = configparser.ConfigParser()
f3.read('nginx.conf')
f3.set('Data','listen','8080')
f3.write(open('nginx.conf.bak2','w'))