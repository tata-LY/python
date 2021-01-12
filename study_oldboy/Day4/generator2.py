#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# 生成器并行

import time

def consumer(name):
    print("{name} 准备吃包子了".format(name=name))
    while True:
        baozi = yield
        print("包子【{baozi}】来了,被{name}吃了".format(baozi=baozi, name=name))

# g = consumer("liuyang")
# g.__next__()
# g.send("玉米馅")
# g.send("韭菜馅")

def producer(name):
    g1 = consumer('A')
    g2 = consumer('B')
    g1.__next__()
    g2.__next__()
    print("老子准备开始吃包子啦！")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子！")
        g1.send(i)
        g2.send(i)

producer("liuyang")