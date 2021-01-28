#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 16:05
# @Author  : liuyang
# @File    : 11.2_module.xml.py
# @Software: PyCharm

# 修改和删除xml文档内容

import xml.etree.ElementTree as ET

tree = ET.parse("11_xml1.xml")
root = tree.getroot()

# 修改
for node in root.iter('year'):
    print(node.text)    # 2012 2015 2015
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")   # 增加属性
tree.write("11_xml1.xml")

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('11_output.xml')
