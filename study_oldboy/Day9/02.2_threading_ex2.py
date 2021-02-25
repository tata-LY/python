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
        print("running task", self.n)
        time.sleep(3)

if __name__ == '__main__':
    for i in range(0, 10):
        t = MyThread(i)
        t.start()
        # t.join()    # = wait()      # 等待线程结束