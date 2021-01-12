#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-30 13:07
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm

"""
函数的参数
函数是绝大多数编程语言中都支持的一个代码的"构建块"，但是Python中的函数与其他语言中的函数还是有很多不太相同的地方，其中一个显著的区别就是Python对函数参数的处理。在Python中，函数的参数可以有默认值，也支持使用可变参数，所以Python并不需要像其他语言一样支持函数的重载，因为我们在定义一个函数的时候可以让它有多种不同的使用方式，下面是两个小例子。
"""
from random import randint

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def sum(a=0, b=0, c=0):
    return a + b + c

# 使用默认参数
print(roll_dice())
# 传参
print(roll_dice(n=3))
print(roll_dice(4))
print(sum())
print(sum(1))
print(sum(1, 2))
print(sum(1, 2, 3))
# 不按顺序
print(sum(c=3, a=1, b=2))

"""
上面的add函数还有更好的实现方案，因为我们可能会对0个或多个参数进行加法运算，而具体有多少个参数是由调用者来决定，我们作为函数的设计者对这一点是一无所知的，因此在不确定参数个数的时候，我们可以使用可变参数，代码如下所示。
"""

def add(*args):
    total = 0
    for i in args:
        print(i)
        total += i
    return total

print(add(1, 2, 3, 4))
# 可以传入0个参数
print(add())

