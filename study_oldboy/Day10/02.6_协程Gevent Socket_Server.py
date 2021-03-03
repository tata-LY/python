#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-3 10:01
# @Author  : liuyang
# @File    : 02.6_协程Gevent Socket.py
# @Software: PyCharm

"""Gevent+Socket实现SocketServer多线程方式"""

import sys
import socket
import time
import gevent

from gevent import socket, monkey

monkey.patch_all()

def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv: ", data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()

def server(port):
    s = socket.socket()
    s.bind(("0.0.0.0", port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)

if __name__ == '__main__':
    server(8001)