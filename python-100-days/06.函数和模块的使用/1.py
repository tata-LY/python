#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-30 11:17
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

"""
输入M和N计算C(M,N)
"""
def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(fac(m) // fac(n) // fac(m - n))
