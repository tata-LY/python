#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-6 13:42
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm
"""
练习3：实现判断一个数是不是素数的函数。
除了1和它本身，没有其他因数
"""

def is_prim(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag

if is_prim(int(input("输入一个正整数："))):
    print("素数！")
else:
    print("不是素数！")