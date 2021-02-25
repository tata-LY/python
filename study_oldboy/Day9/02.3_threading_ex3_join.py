#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-25 8:44
# @Author  : liuyang
# @File    : 02.1_threading_ex1.py
# @Software: PyCharm
"""join等待子线程执行完毕"""

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
        time.sleep(self.sleep_time)

if __name__ == '__main__':
    start_time = time.time()
    t1 = MyThread('t1', 4)
    t2 = MyThread('t2', 2)
    t3 = MyThread('t3', 3)
    t1.start()
    t2.start()
    t3.start()

    """join等待子线程执行完毕"""
    t1.join()
    t2.join()
    t3.join()
    end_time = time.time()
    print('all task done, cost: %s' % (end_time-start_time))    # all task done, cost: 4.001687049865723