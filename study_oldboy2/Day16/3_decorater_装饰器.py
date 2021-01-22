#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-22 13:07
# @Author  : liuyang
# @File    : 3_decorater_装饰器.py
# @Software: PyCharm
import time

def show_time1(f):
    def wrapper(a, b, c):
        start = time.time()
        f(a, b, c)
        print(a, b, c)
        print('ok')
        end = time.time()
        print('花费时间：%s' % (end - start))
    return wrapper

@show_time1
def test1(a, b, c):
    print(a+b+c)
    print('ok')
    time.sleep(1)

