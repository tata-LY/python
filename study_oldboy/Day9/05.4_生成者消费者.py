#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-26 13:27
# @Author  : liuyang
# @File    : 05.4_生成者消费者.py
# @Software: PyCharm

import threading, time
import queue

q = queue.Queue(maxsize=10)     # 最多10个队列

def Producer(name):
    count = 1
    while True:
        time.sleep(0.5)
        q.put("骨头%s" % count)
        print("生产了[骨头%s]" % count)
        count += 1

def Consumer(name):
    while True:
        time.sleep(2)
        print("[%s] 取到 [%s],并且吃了它..." % (name, q.get()))


p = threading.Thread(target=Producer, args=("ALEX", ))
c1 = threading.Thread(target=Consumer, args=("zhangjuan", ))
c2 = threading.Thread(target=Consumer, args=("liuyang", ))

p.start()
c1.start()
c2.start()