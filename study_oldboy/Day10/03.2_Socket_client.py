#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-4 10:25
# @Author  : liuyang
# @File    : 03.2_Socket_client.py
# @Software: PyCharm

import socket

HOST = 'localhost'
PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = input(">>>").strip()
    s.sendall(msg.encode("utf-8"))
    data = s.recv(1024).decode("utf-8")

    print("received：", data)

s.close()