#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-22 10:59
# @Author  : liuyang
# @File    : 2_闭包.py
# @Software: PyCharm


"""
闭包就是内部函数+定时函数时的环境
"""

def outer():
    x = 10
    def inner():
        print(x)
    return inner

f = outer()
f()