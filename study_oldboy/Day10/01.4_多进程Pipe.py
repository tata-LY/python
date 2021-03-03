#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-2 9:31
# @Author  : liuyang
# @File    : 01.4_多进程Pipe.py
# @Software: PyCharm

"""
Pipe管道，一头send数据，一头recv数据。
"""

from multiprocessing import Process, Pipe
from threading import Thread


def f(conn):
    conn.send([42, None, 'hello'])
    conn.send([43, None, 'hello'])
    print(conn.recv())      # 接收parent_conn发送的  from parent send
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    # p = Thread(target=f, args=(child_conn, ))     # 线程
    p.start()
    print(parent_conn.recv())  # [42, None, 'hello']
    print(parent_conn.recv())  # [43, None, 'hello']
    parent_conn.send("from parent send")
    p.join()
