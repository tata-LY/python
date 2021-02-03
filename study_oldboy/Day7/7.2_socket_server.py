#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-2 13:46
# @Author  : liuyang
# @File    : 7.2_socket_server.py
# @Software: PyCharm
import os
import socket
server = socket.socket()
server.bind(('127.0.0.1', 6969))        # 绑定要监听的端口
server.listen(5)     # 监听 并发数

print("我要开始等电话了")
while True:
    conn, addr = server.accept()  # 等电话打进来
    # conn就是客户端连过来而在服务器端为期生成的一个连接实例
    print(conn)  # <socket.socket fd=856, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 6969), raddr=('127.0.0.1', 53363)>
    print(addr)  # ('127.0.0.1', 53363)
    print("电话来了")

    while True:
        data = conn.recv(10240000)
        # print("recv: ", data.decode())
        if not data:
            print("client has lost...")
            break
        data = data.decode("utf-8")
        res = os.popen(data).read()
        conn.sendall(res.encode("utf-8"))

server.close()