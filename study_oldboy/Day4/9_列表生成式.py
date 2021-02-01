#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 15:37
# @Author  : liuyang
# @File    : 9_列表生成式.py
# @Software: PyCharm

l1 = []
for i in range(10):
    l1.append(i*2)

l2 = [i*2 for i in range(10)] # 列表生成器

print(l1)       # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(l2)       # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]