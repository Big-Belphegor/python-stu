__author__ = "Alien"
from urllib.request import urlopen
import json

# 指定json文件url
json_url = 'https://raw.githubusercontent.com/nlohmann/json/develop/benchmarks/data/jeopardy/jeopardy.json'
# 下载此json文件
response = urlopen(json_url)
# 读取数据
req = response.read()
# 将数据写入文件
with open('jeopardy_test.json','wb') as file:
    file.write(req)

# 加载json格式
file_urllib = json.load(req)
print(file_urllib)