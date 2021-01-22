#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-22 10:21
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

import time

# 计算函数test1()运行的时间
def test1():
    start = time.time()
    time.sleep(1)
    print('in the func test1()')
    end = time.time()
    print('花费时间：%s'% (end-start))
test1()


def show_time2(f):
    start = time.time()
    f()
    end = time.time()
    print('花费时间：%s'% (end-start))
def test2():
    time.sleep(1)
    print('in the func test2()')
show_time2(test2)


def show_time3(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('花费时间：%s' % (end - start))
    return inner
def test3():
    time.sleep(1)
    print('in the func test3()')
show_time3(test3)()


def show_time4(f):
    def wrapper():
        start = time.time()
        f()
        end = time.time()
        print('花费时间：%s' % (end - start))
    return wrapper
@show_time4
def test4():
    time.sleep(1)
    print('in the func test4()')
test4()