#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-6 13:18
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm
"""
练习1：实现计算求最大公约数和最小公倍数的函数。
最大公约数：最大公约数是能被x,y整除的最大的数
最大公倍数=X*y//最大公约数
"""

def gcd(x, y):
    """最大公约数"""
    if x > y:
        x, y = y, x
    for fator in range(x, 0, -1):
        if x % fator == 0 and y % fator == 0:
            return fator
            break

def lcm(x, y):
    fator = gcd(x, y)
    return x * y // fator

print(gcd(20, 6))
print(lcm(20, 6))