__author__ = "Alien"

# JSON模块，数据存储
import json                             # 导入json模块

number = [1,2,3,4,5]                    # 创建要导入的列表
filename = 'number.json'                # 指定json文件，通常以.json结尾

with open(filename,'w') as file:
    json.dump(number,file)              # 用json.dump()写入列表到文件
