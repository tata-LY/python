#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 15:53
# @Author  : liuyang
# @File    : 11.1_module_xml.py
# @Software: PyCharm

"""
xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单。
不过，古时候，在json还没诞生的黑暗年代，大家只能选择用xml呀，至今很多传统公司如金融行业的很多系统的接口还主要是xml。
"""
# xml查看

"""
xml1内容
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year updated="yes">2010</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year updated="yes">2013</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year updated="yes">2013</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
"""

import xml.etree.ElementTree as ET

tree = ET.parse("11_xml1.xml")
root = tree.getroot()
print(root) # <Element 'data' at 0x0000021840A2E630>
print(root.tag) # data

# 遍历xml文档
# tag：标签； attrib：属性；text：内容
for child in root:
    print(child.tag, child.attrib)  # country {'name': 'Liechtenstein'}
    for i in child:
        print('\t', i.tag, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)
"""
year 2010
year 2013
year 2013
"""