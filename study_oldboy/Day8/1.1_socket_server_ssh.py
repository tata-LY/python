#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-3 14:48
# @Author  : liuyang
# @File    : 1_socket_server_ssh.py
# @Software: PyCharm

import  socket, os, time
server = socket.socket()
server.bind(('127.0.0.1', 9999))

server.listen()
while True:
    print("等待新指令...")
    conn, addr = server.accept()
    print("new conn: ", addr)
    while True:
        data = conn.recv(1024).decode("utf-8")
        if not data:
            print("客户端已断开")
            break
        print("执行指令: ", data)

        cmd_res = os.popen(data).read()     # 接受字符串，执行结果也是字符串
        if len(cmd_res) == 0:
            cmd_res = "命令错误"
        conn.send(str(len(cmd_res)).encode("utf-8"))       # 先发大小给客户端
        # time.sleep(0.5)     # 临时使用此方法防止粘包
        client_ack = conn.recv(1024) # 等客户端去确认，防止粘包
        # print("ack from client: ", client_ack)
        conn.send(cmd_res.encode("utf-8"))  # python3 二进制发送

server.close()

