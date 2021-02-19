#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-4 14:28
# @Author  : liuyang
# @File    : 3.2_socketServer_client_基本.py
# @Software: PyCharm
import socket

client = socket.socket()     # 声明socket类型，同时生成socket连接对象
client.connect(('192.168.113.11', 9999))

while True:
    msg = input(">>>: ").strip()
    if len(msg) ==0:continue    # 不能发空
    client.send(msg.encode("utf-8"))     # python3不能发str
    data = client.recv(10240000)
    print("recv：", data.decode("utf-8"))
    # print(data.decode("utf-8"))

client.close()