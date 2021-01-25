#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-25 16:30
# @Author  : liuyang
# @File    : 11_生成器并行.py
# @Software: PyCharm

import time

def consumer(name):
    print("{name} 准备吃包子了".format(name=name))
    while True:
        baozi = yield
        print("包子【{baozi}】来了,被{name}吃了".format(baozi=baozi, name=name))

g = consumer("liuyang")
g.__next__()
g.send("玉米馅")
g.send("韭菜馅")
"""
liuyang 准备吃包子了
包子【玉米馅】来了,被liuyang吃了
包子【韭菜馅】来了,被liuyang吃了
"""

time.sleep(3)

def producer(name):
    g1 = consumer('刘洋')
    g2 = consumer('张娟')
    g1.__next__()
    g2.__next__()
    print("老子准备开始吃包子啦！")
    for i in range(1, 11):
        time.sleep(2)
        print("做了第%d个包子！" % i)
        g1.send(i)
        g2.send(i)

producer("liuyang")