#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-30 11:03
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm
"""
输出100以内所有的素数。

说明：素数指的是只能被1和自身整除的正整数（不包括1）。
"""

for i in range(2, 101):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        print(i)