__author__ = "Alien"
import configparser

# Python内置的用于写配置文件的模块，效果可以看nginx.conf文件
f = configparser.ConfigParser()

f["Data"] = {
    'Listen':'80',
    'server_name':'test.com'
}

with open('nginx.conf','w') as d:
    f.write(d)