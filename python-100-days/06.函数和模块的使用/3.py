#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-30 13:26
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm


"""
对于任何一种编程语言来说，给变量、函数这样的标识符起名字都是一个让人头疼的问题，因为我们会遇到命名冲突这种尴尬的情况。最简单的场景就是在同一个.py文件中定义了两个同名函数，由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，也就意味着两个函数同名函数实际上只有一个是存在的。
"""

def foo():
    print('hello, world!')

def foo():
    print('goodbye, world!')

# 下面的代码会输出什么呢？
foo()

from module1 import foo
foo()

from module2 import foo
foo()

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

import module3