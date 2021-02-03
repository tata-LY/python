#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-2 13:41
# @Author  : liuyang
# @File    : 7.1_socket_client.py
# @Software: PyCharm
import socket

client = socket.socket()     # 声明socket类型，同时生成socket连接对象
client.connect(('127.0.0.1', 6969))

while True:
    msg = input(">>>: ").strip()
    if len(msg) ==0:continue    # 不能发空
    client.send(msg.encode("utf-8"))     # python3不能发str
    data = client.recv(10240000)
    # print("recv：", data.decode("utf-8"))
    print(data.decode("utf-8"))

client.close()