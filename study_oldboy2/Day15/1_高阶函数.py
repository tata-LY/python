#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 16:24
# @Author  : liuyang
# @File    : 1_高阶函数.py
# @Software: PyCharm

def add(x, y, f):
    return f(x) + f(y)

res = add(3, -6, abs)
print(res)


def f(n):
    return n**2
def foo(a, b, func):
    return func(a) + func(b)

print(foo(3, 4, f))
