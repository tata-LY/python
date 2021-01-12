#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# 修改和删除xml文档内容

import xml.etree.ElementTree as ET

tree = ET.parse("xml1.xml")
root = tree.getroot()

# 修改
for node in root.iter('year'):
    print(node.text)
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")   # 增加属性

tree.write("xml1.xml")

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')