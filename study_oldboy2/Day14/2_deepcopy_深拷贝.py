#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 13:51
# @Author  : liuyang
# @File    : 2_深拷贝.py
# @Software: PyCharm

import copy

"""
copy.deepcopy 深拷贝
- 拷贝所有层，修改拷贝的任何层数据，原数据都不会改变。
"""

a1 = [[1], [2], 3, 4]
a2 = copy.deepcopy(a1) # 拷贝
a3 = a1
a2[0][0] = 'a'
a3[1][0] = 'A'
print('a1: ', a1)   # [['a'], ['A'], 3, 4] # 列表修改第2+层值，通过直接赋值（a3=a1）方式会改变原a1的值;通过copy.deepcopy(a1)方式不会修改a1的值。
print('a2: ', a2)   # [['a'], ['A'], 3, 4]
print('a3: ', a3)   # [['a'], ['A'], 3, 4]

a2[2] = 'b'
a3[3] = 'B'
print('a1: ', a1)   # [['a'], ['A'], 3, 'B'] # 列表修改第1层值，通过直接赋值（a3=a1）方式会改变原a1的值;通过copy(a2 = a1.copy())方式不会修改a1的值。
print('a2: ', a2)   # [['a'], ['A'], 'b', 4]
print('a3: ', a3)   # [['a'], ['A'], 3, 'B']