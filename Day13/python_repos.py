__author__ = "Alien"
import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ",r.status_code)        # 获取URL的响应状态

# 将API响应存储在一个变量中,转为python字典
response_dict = r.json()


# 处理结果
# 查看都有哪些Key
# print(response_dict.keys())

# GitHub当前一共有的python语言仓库个数
print('Total repostiories: ',response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned: ',len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
print('\nKeys: ',len(repo_dict))
# for key in sorted(repo_dict.keys()):      # 查看并排序此仓库的所有key
#     print(key)

print('This repertory User ID: ',repo_dict['id'])
print('Owner: ',repo_dict['owner']['login'])

