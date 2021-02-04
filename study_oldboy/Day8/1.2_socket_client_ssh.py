#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-3 14:52
# @Author  : liuyang
# @File    : 1.2_socket_client_ssh.py
# @Software: PyCharm

import socket
client = socket.socket()

client.connect(('127.0.0.1', 9999))
while True:
    cmd = input("命令>>>").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode("utf-8"))        # python3 二进制发送
    cmd_res_size = int(client.recv(1024).decode("utf-8"))        # 接受命令结果的长度，二进制转成int
    print("命令结果大小：", cmd_res_size)
    client.send("客户端已经准备好接收了，服务端可以发数据了".encode())   # 解决粘包问题
    cmd_res = ''
    while True:
        cmd_res += client.recv(1024).decode("utf-8")        # 循环接收server send过来的数据
        if len(cmd_res) == cmd_res_size:break
    print(cmd_res)

client.close()
