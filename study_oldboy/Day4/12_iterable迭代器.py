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
print('')

a2 = iter(x*x for x in range(5))
while True:
    try:
        x = next(a2)
        print("fib_gen1: ", x, end=' | ') # fib_gen1:  0 | fib_gen1:  1 | fib_gen1:  4 | fib_gen1:  9 | fib_gen1:  16 |
    except StopIteration as e:
        print('\nGenerator return value: ', e.value) # Generator return value:  done   会打印result的值
        break