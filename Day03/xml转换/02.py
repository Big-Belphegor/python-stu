__author__ = "Alien"

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
head = tree.getroot()           # 获取xml的标签头，如本例中的data
print(head.tag)

# 遍历xml文档
for body in head:               # 获取第二层的标签头及标签属性
    print(body.tag, body.attrib)
    for i in body:              # 获取第三层的标签头及标签属性
        print(i.tag, i.text)

# 只遍历year节点
for node in head.iter('year'):  # 获取第二层标签头为‘year’
    print(node.tag, node.text)


    # 来自：http://www.cnblogs.com/alex3714/articles/5161349.html