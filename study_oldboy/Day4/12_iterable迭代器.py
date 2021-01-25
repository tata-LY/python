#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 16:51
# @Author  : liuyang
# @File    : 12_iterable迭代器.py
# @Software: PyCharm

# from collections import Iterable,Iterator
from collections.abc import Iterable, Iterator # collections3.3-3.9替代为collections.abc

# 判断是否可迭代
print(isinstance('abc', Iterable))      # True
print(isinstance((x*x for x in range(10)), Iterator))       # True
# 判断是否为列表
print(isinstance([1, 3], list))     # True

a = [x*x for x in range(10)]
print(a)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
a = iter(a)
print(a)    # <list_iterator object at 0x000001BA175427C0>

print(a.__next__())     # 0
print(a.__next__())     # 1
print(a.__next__())     # 4

for i in a:
    print(i, end=' ')   # print(a.__next__())