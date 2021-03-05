#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-4 10:12
# @Author  : liuyang
# @File    : 03.1_Select.py
# @Software: PyCharm

import select
import socket
import sys
import queue

# Create a TCP/IP socket
server = socket.socket()
server.bind(('localhost', 9000))
server.listen(1000)

server.setblocking(False)       # 不阻塞

msg_dic = {}

inputs = [server, ]     # 自己也要监测呀,因为server本身也是个fd
# inputs = [server,conn] #[conn,]
# inputs = [server,conn,conn2] #[conn2,]
outputs = []
# outputs = [r1]

while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)
    for r in readable:
        if r is server:     # 代表来了一个新连接
            conn, addr = server.accept()
            conn.setblocking(0)
            print("来了个新连接", addr)
            inputs.append(conn)     # 因为这个新建立的连接还没发数据过来，现在就接收的话程序就报错了，所以要想实现这个客户端发数据来时server端能知道，就需要让select再监测这个conn
            msg_dic[conn] = queue.Queue() # 初始化一个队列，后面存要返回给这个客户端的数据
        else:   # r不是server的话，那就是现有的连接来数据了（fd）
            data = r.recv(1024).decode("utf-8")
            if data:
                print("收到数据：", data)
                msg_dic[r].put(data)
                if r not in outputs:
                    outputs.append(r)   # 放入放回的连接队列里
                # r.send(data.encode("utf-8"))
                # print("send done...")
            else: # 如果收不到data，代表客户端断开了
                print("客户端断开了", r)
                if r in outputs: outputs.remove(r) # 清理已断开的连接
                inputs.remove(r)    # 清理已断开的连接
                del msg_dic[r]      # 清理已断开的连接

    for w in writeable: # 要返回给客户端的连接列表
        data_to_client = msg_dic[w].get_nowait()
        w.send(data_to_client.encode("utf-8"))
        outputs.remove(w)   # 确保下次循环的时候writeable不返回这个已经处理完的连接了

    for e in exceptional:   # 客户端断开连接
        if e in outputs:outputs.remove(e)
        inputs.remove(e)
        e.close()
        del msg_dic[e]