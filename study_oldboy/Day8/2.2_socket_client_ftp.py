#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-3 14:52
# @Author  : liuyang
# @File    : 1.2_socket_client_ssh.py
# @Software: PyCharm

import socket
import hashlib
client = socket.socket()

client.connect(('192.168.113.11', 9999))
while True:
    cmd= input("CMD>>>").strip()
    if len(cmd) == 0:continue
    if cmd.startswith("get"):     # 判断是否是get命令开头
        client.send(cmd.encode("utf-8"))
        file_size = int(client.recv(1024).decode("utf-8")) # 文件大小
        print("服务端文件大小: ", file_size)
        client.send("接收服务端文件大小完成，服务端可以传输文件了，客户端准备去接收文件".encode("utf-8"))    # 通知服务端开始传输文件内容
        receiced_size = 0
        filename = cmd.split()[1]
        f = open(filename, "w")
        m = hashlib.md5()
        while receiced_size < file_size:
            """这里采用接收一次，就写入一次，防止接收的文件数据过大大量占用内存"""

            """
            Alex老师这里解决粘包问题的方法：通过判断receiced_size-file_size是否大于1024，如果大于1024，下次还是接收1024byte的数据；如果小于1024，下次接收receiced_size-file_size大小的数据。
            此方法有个bug，如果md5的数据刚刚好卡在1024的节点上，就会有问题。比如最后剩下1032byte的数据，其中1011到1032这一段的数据是md5，按上述方法接收数据，最后一次接收的数据就会包括md5数据，然后接收md5数据时会缺失。
            还是采用client端发送消息通知server端，server再发送md5数据，client端再接收md5数据。
            """
            # if receiced_size - file_size > 1024:
            #     size = 1024
            # else:
            #     size = receiced_size - file_size
            # data = client.recv(size).decode("utf-8")

            data = client.recv(1024).decode("utf-8")
            m.update(data.encode())     # client端接收的文件md5
            receiced_size += len(data)
            f.write(data)
            # print(file_size, receiced_size)
        else:
            new_file_md5 = m.hexdigest()
            f.close()
            print("文件接收完成,接收到的文件大小：", receiced_size)
            client.send("文件接收完成,服务端可以发送md5了".encode("utf-8"))   # 通知服务端发送md5,解决粘包问题

        server_file_md5 = client.recv(1024).decode("utf-8") # 接收server端send过来的文件md5
        print("服务端文件的md5: ", server_file_md5)
        print("客户端文件的md5: ", new_file_md5)
    else:
        print("命令不正常，重新输入：")

client.close()
