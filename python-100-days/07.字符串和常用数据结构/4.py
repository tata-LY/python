#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-8 11:09
# @Author  : liuyang
# @File    : 4.py
# @Software: PyCharm
"""
元组
Python中的元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，不同之处在于元组的元素不能修改，在前面的代码中我们已经不止一次使用过元组了。顾名思义，我们把多个元素组合到一起就形成了一个元组，所以它和列表一样可以保存多条数据。下面的代码演示了如何定义和使用元组。
"""
t = ('liuyang', 29, '男', '湖南华容')
print(t)
print(t[1:3])
for member in t:
    print(member)
# t[0] = '刘洋' # 不支持修改
t = ('刘洋', 29, '男', '湖南华容')
print(t)
l = list(t)
print(l)
l.append('安信证券')
t = tuple(l)
print(t)