#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-25 8:44
# @Author  : liuyang
# @File    : 02.1_threading_ex1.py
# @Software: PyCharm
"""直接调用线程"""

import threading
import time

def run(n):
    print("task", n)
    time.sleep(2)

# t1 = threading.Thread(target=run, args=('t1',))
# t2 = threading.Thread(target=run, args=('t2',))
# t1.start()
# t2.start()

# run("T1")
# run("T2")


for i in range(10):
    t = threading.Thread(target=run, args=(i,))     # 生成一个线程实例
    t.start()       # 启动线程
    # print(t.getName()) # 获取线程名