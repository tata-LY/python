#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 16:29
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

"""
# 寻找水仙花数。
# 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
例如：$1^3 + 5^3+ 3^3=153。
"""

for i in range(100, 1000):
    a = i % 10
    b = i % 100 // 10
    c = i // 100
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)