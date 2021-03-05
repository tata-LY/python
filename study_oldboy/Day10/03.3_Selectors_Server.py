#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-4 13:53
# @Author  : liuyang
# @File    : 03.3_Selectors_Server.py
# @Software: PyCharm

import selectors
import socket
import time

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    print("mask: ", mask)       # mask:  1
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)  # 新连接注册read回调函数


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
        time.sleep(1)   # 不允许再次recv，BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
        data2 = conn.recv(1024)
        print(data2)
        # conn.send(b'2222222222')  # 可以多次send
        # conn.send(b'3333333333')
        # conn.send(b'4444444444')
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)    # 新连接过来调用accept

while True:
    events = sel.select()   # 默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)     # key.fileobj=文件句柄