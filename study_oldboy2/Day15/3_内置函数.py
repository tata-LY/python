#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-22 8:47
# @Author  : liuyang
# @File    : 3_内置函数.py
# @Software: PyCharm

"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
"""
print('filter()'.center(70, '-'))
s1 = [1, 2, 3, 4]
def f1(s):
    if s != 1:
        return s**2

ret = filter(f1, s1)
print(ret, type(ret), list(ret)) # 迭代器 <filter object at 0x000002C5068C9BE0> <class 'filter'> [2, 3, 4] # 赋值为满足条件的参数
print(ret, type(ret), list(ret)) # <filter object at 0x000002C5068C9BE0> <class 'filter'> [] 第二次就拿不到里面的值了

"""
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
"""
print('map()'.center(70, '-'))
ret = map(f1, s1)
print(ret, type(ret), list(ret)) # <map object at 0x000001C5E6E99FD0> <class 'map'> [None, 4, 9, 16] 不满足的用None补充,赋值为函数的return
print(ret, type(ret), list(ret)) # <map object at 0x00000271FDB6E9D0> <class 'map'> []

"""
reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
"""
print('reduce()'.center(70, '-'))
from functools import reduce
def f2(x, y):
    return x + y
ret = reduce(f2, range(1, 101))
print(ret)

"""
lambda
普通函数与匿名函数的对比：
"""
print('lambda'.center(70, '-'))
# 普通函数
def add(a, b):
    return a + b
print(add(2, 3))

# 匿名函数
add = lambda a, b: a + b
print(add(2, 3))

ret = reduce(lambda x,y: x+y, range(1, 101))
print(ret)

ret = map(lambda x: x**2, range(1, 10)) # ret赋值为函数的return
print(tuple(ret))

ret = filter(lambda x: x**2, range(1, 10)) # ret赋值为满足条件的参数
print(list(ret))