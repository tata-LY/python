#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-3 10:08
# @Author  : liuyang
# @File    : 02.7_Socket_Client.py
# @Software: PyCharm

import socket

HOST = 'localhost'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = bytes(input(">>>"), encoding="utf-8")
    s.sendall(msg)
    data = s.recv(1024)

    print("received", repr(data))

s.close()
