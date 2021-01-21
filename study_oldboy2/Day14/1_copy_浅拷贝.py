#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 13:22
# @Author  : liuyang
# @File    : 1_深浅拷贝.py
# @Software: PyCharm

"""copy 浅拷贝"""
s1 = [1, 2, 3]
s3 = s1.copy()  # 不会改变
s2 = s1     # 这样赋值，s1和s2会一起改变
s2[0] = 'a'
print(s1)   # ['a', 2, 3] s1跟着s2也变化了
print(s2)   # ['a', 2, 3]
print(s3)   # [1, 2, 3]

a1 = [[1], [2], 3, 4]
a2 = a1.copy()  # 浅拷贝，只会拷贝第一层。不会拷贝以后的层
a3 = a1
a2[0][0] = 'a'
a3[1][0] = 'A'
print('a1: ', a1)   # [['a'], ['A'], 3, 4] # 列表修改第2+层值，通过直接赋值（a3=a1）、copy(a2 = a1.copy())方式都会改变原a1的值。
print('a2: ', a2)   # [['a'], ['A'], 3, 4]
print('a3: ', a3)   # [['a'], ['A'], 3, 4]

a2[2] = 'b'
a3[3] = 'B'
print('a1: ', a1)   # [['a'], ['A'], 3, 'B'] # 列表修改第1层值，通过直接赋值（a3=a1）方式会改变原a1的值。通过copy(a2 = a1.copy())方式不会修改a1的值。
print('a2: ', a2)   # [['a'], ['A'], 'b', 4]
print('a3: ', a3)   # [['a'], ['A'], 3, 'B']

a = 1
b = a
b = 2
print(a, b) # 1 2 字符形式不会修改

