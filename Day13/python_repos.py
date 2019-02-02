__author__ = "Alien"
import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
url_limit = 'https://api.github.com/rate_limit'
r = requests.get(url)
r2 = requests.get(url_limit)
# print("Status code: ",r.status_code)        # 获取URL的响应状态
# print("Status code: ",r2.status_code)        # 获取URL的响应状态

# 将API响应存储在一个变量中,转为python字典
response_dict = r.json()
response_limit = r2.json()

# 处理结果
# 查看都有哪些Key
# print(response_dict.keys())

# GitHub限制
response_limit_keys = response_limit.keys()
print('Repositories returned: ',len(response_limit_keys))

response_limit_resource = response_limit['resources']
response_limit_search = response_limit_resource['search']
for key,value in response_limit_search.items():
    print('%s: %s' % (key,value))

# # GitHub当前一共有的python语言仓库个数
# print('Total repostiories: ',response_dict['total_count'])
#
# # 探索有关仓库的信息
# repo_dicts = response_dict['items']
# print('Repositories returned: ',len(repo_dicts))
#
# # 研究第一个仓库
# repo_dict = repo_dicts[0]
# print('\nKeys: ',len(repo_dict))
# # for key in sorted(repo_dict.keys()):      # 查看并排序此仓库的所有key
# #     print(key)
#
# print('This repertory User ID: ',repo_dict['id'])
# print('Owner: ',repo_dict['owner']['login'])



