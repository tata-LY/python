#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-25 8:44
# @Author  : liuyang
# @File    : 02.1_threading_ex1.py
# @Software: PyCharm
"""循环时，join计算所有线程运行使用时间"""

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, n, sleep_time):
        super(MyThread, self).__init__()
        # threading.Thread.__init__(self)   # 继承的另外一种方式
        self.n = n
        self.sleep_time = sleep_time


    def run(self):
        print("running task", self.n)
        # print("子线程：%s|活动的线程个数：%s" % (threading.current_thread(), threading.active_count()))
        time.sleep(self.sleep_time)

if __name__ == '__main__':
    start_time = time.time()
    t_objs = []     # 列表，存放线程实例t
    for i in range(1, 5):
        t = MyThread(i, i)
        t.start()
        t_objs.append(t)        # 为了不阻塞后面线程的启动，不再这里join，先放到一个列表里

    for t in t_objs:        # 循环线程实例列表，等待所有线程执行完毕
        t.join()
    end_time = time.time()
    print('all task done, cost: %s' % (end_time-start_time))    # all task done, cost: 5.0014424324035645
    print("主线程：%s|活动的线程个数：%s" % (threading.current_thread(), threading.active_count()))     # 主线程：<_MainThread(MainThread, started 12868)>|活动的线程个数：1