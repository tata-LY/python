#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-11 10:22
# @Author  : liuyang
# @File    : 4.py
# @Software: PyCharm
"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
"""
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

print(max2((55,7, 4)))