#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-8 14:47
# @Author  : liuyang
# @File    : 6.py
# @Software: PyCharm
"""
使用字典
"""
family = {'liuyang': 29, 'zj': 28}
print(family, family['liuyang'])

# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)

for key in family:
    print(key, family[key])
family.update(ldk=52, ssy=50, zjh=51, rll=50)
print(family)
if 'liuyang' in family:
    print('liuyang is in family!')

# 删除字典中的元素(最后一个)
print(family.popitem())
print(family.pop('liuyang', 29))
print(family)

# 清空字典
family.clear()
print(family)