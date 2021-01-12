#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 13:34
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

"""
用for循环实现1~100求和
"""
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 用for循环实现1~100 偶数求和
sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)

# 用for循环实现1~100之间的偶数求和（使用if）
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)