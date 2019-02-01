__author__ = "Alien"
import csv

# 从CSV文件中获取数据

# 打开CSV文件
filename = 'check_work_attend.csv'
with open(filename) as file:
    reader = csv.reader(file)
    # 先打印CSV文件的第一行(获取字段)
    # header_row = next(reader)       # 运行一次读一行
    # print(header_row)
    # 将字段的索引及其值打印，方便分析要截取的数据部分
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    people = []
    for row in reader:
        if row[1] != '':
            people.append(row[1])

    print(people)