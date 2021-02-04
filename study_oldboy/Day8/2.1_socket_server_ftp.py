#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-3 14:48
# @Author  : liuyang
# @File    : 1_socket_server_ssh.py
# @Software: PyCharm

import  socket, os, time
import hashlib
server = socket.socket()
server.bind(('0.0.0.0', 9999))

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
        cmd, filename = data.split()
        print("%s开始下载%s文件" % (addr,filename))
        if os.path.isfile(filename):
            f = open(filename, "r")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode("utf-8"))  # 发送文件大小
            conn.recv(1024) # 等待接收文件大小确认，解决粘包
            for line in f:  # 一行一行循环，防止大文件占用内存
                m.update(line.encode())
                conn.send(line.encode("utf-8"))
            print("file md5: ", m.hexdigest())
            f.close()
            # time.sleep(0.5)   # 使用sleep临时解决粘包问题
            conn.recv(1024) # 等待文件传输完成确认，防止粘包
            conn.send(m.hexdigest().encode("utf-8"))   # 发送md5
        print("done")
server.close()

