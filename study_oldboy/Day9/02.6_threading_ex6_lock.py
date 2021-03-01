#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-25 8:44
# @Author  : liuyang
# @File    : 02.6_threading_ex6_lock.py
# @Software: PyCharm

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        # threading.Thread.__init__(self)   # 继承的另外一种方式
        self.n = n
        self.lock = threading.Lock()    # 生成锁实例

    def run(self):
        self.n += 1
        global num      # 定义一个全局变量 在每个线程中都获取这个全局变量
        self.lock.acquire()     # 修改数据前加锁
        num += 1
        print("n:%s num:%s" % (self.n, num))
        time.sleep(2)
        self.lock.release()     # 修改后释放

if __name__ == '__main__':
    n = 0
    num = 0
    t_objs = []
    for i in range(0, 10):
        t = MyThread(n)
        # t.setDaemon(True)  # 将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
        t.start()
        t_objs.append(t)

    for t in t_objs:    # 等待所有线程执行完毕
        t.join()
    print('所有任务都已结束 n:%s num:%s' % (n,num))     # 所有任务都已结束 n:0 num:1000

