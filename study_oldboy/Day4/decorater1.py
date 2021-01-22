#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import time

def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return warpper()

@timmer
def test1():
    time.sleep(1)
    print("in the test1")

test1()