#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 10:53
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm

"""
分段函数求值
if 嵌入
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

"""

x = float(input("x = "))
if x > 1:
    y = 3 * x -5
else:
    if -1 <= x <= 1:
        y = x + 2
    elif x < -1:
        y = 5 * x + 3

print("f(%.2f) = %.2f" % (x, y))