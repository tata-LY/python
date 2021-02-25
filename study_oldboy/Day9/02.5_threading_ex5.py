#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-25 8:44
# @Author  : liuyang
# @File    : 02.1_threading_ex1.py
# @Software: PyCharm
"""继承方式调用线程"""

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        # threading.Thread.__init__(self)   # 继承的另外一种方式
        self.n = n

    def run(self):
        self.n += 1
        print(self.n)

if __name__ == '__main__':
    n = 1
    t_objs = []
    for i in range(0, 5):
        t = MyThread(n)
        t.setDaemon(True)  # 将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
        t.start()
        t_objs.append(t)
    for t in t_objs:
        t.join()
    print('n:%s' % n)       # n:1

"""
2
2
2
2
2
n:1
"""
