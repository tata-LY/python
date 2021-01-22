#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import time

# 高阶函数
def bar():
    print("in the bar")
    time.sleep(2)

def test1(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time is %s" %(stop_time-start_time))

test1(bar)

def test2(func):
    print(func)
    return func

# print(test2(bar))
bar = test2(bar)
bar()