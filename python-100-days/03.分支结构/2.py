#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 10:21
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm

"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

"""

x = float(input("x = "))
if x >1:
    y = 3 * x - 5
elif -1 <= x <=1:
    y = x + 2
elif x < -1:
    y = 5 * x + 3

print('f(%.2f) = %.2f' % (x, y))