#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-5 16:16
# @Author  : liuyang
# @File    : 03.6_Selectors_server.py
# @Software: PyCharm

import selectors
import socket
import time

class FtpServer(object):
    def __init__(self, conn):
        self.conn = conn

    def handle(self):
        try:
            self.data = self.conn.recv(1024).decode('utf-8')
            if self.data:
                action = self.data
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(action)
                else:
                    self.conn.send(b'no func')
            else:
                print('closing', self.conn)
                sel.unregister(self.conn)
                self.conn.close()

        except Exception as e:
            print("ERR: ", e)
            sel.unregister(self.conn)
            self.conn.close()

    def ls(self, *args):
        print('ls')
        self.conn.send(b'LS')

    def put(self, *args):
        print('put')
        self.conn.send(b'PUT')

    def get(self, *args):
        print('get')
        self.conn.send(b'GET')



def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)  # 新连接注册read回调函数


def read(conn, mask):
    ftp_server = FtpServer(conn)
    ftp_server.handle()

sel = selectors.DefaultSelector()
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
