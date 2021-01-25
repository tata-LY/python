#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 13:09
# @Author  : liuyang
# @File    : 3_decorater.py
# @Software: PyCharm

import time
def bar():
    print('in the func bar')
    time.sleep(2)

def test1(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print('the func run time is %s' % (stop_time-start_time))

test1(bar)

def test2(func):
    print(func)
    return func

t=test2(bar)
bar()
t() # t() = bar()