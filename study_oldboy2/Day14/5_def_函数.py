#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 14:56
# @Author  : liuyang
# @File    : 5_def_函数.py
# @Software: PyCharm

import  time
def logger():
    time.sleep(1)
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('5.log','a+') as f:
        f.write('%s end action\n' %time_current)

def test1():
    print('in the test1')

    logger()
def test2():
    print('in the test2')

    logger()
def test3():
    print('in the test3')
    logger()

test1()
test2()
test3()
