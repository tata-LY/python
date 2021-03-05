#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-5 9:56
# @Author  : liuyang
# @File    : ftp_server.py
# @Software: PyCharm

import os, sys
import selectors, socket
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main, logger
from conf import settings


def server_accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    logger.logger('INFO', '新连接：%s' % conn)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, handle)  # 新连接注册main.handle回调函数
    dic[conn] = {}

def handle(conn, mask):
    try:
        data = conn.recv(1024).decode("utf-8")  # Should be ready
        if data:
            cmd_dic = json.loads(data)
            print(cmd_dic)
            action = cmd_dic['action']
            opration = main.Operation(conn)
            if hasattr(opration, action):
                func = getattr(opration, action)
                func(cmd_dic)
        else:
            print("断开连接：", conn)
            logger.logger('INFO', '断开连接：%s' % conn)
            sel.unregister(conn)
            conn.close()
    except Exception as e:
        print(e, conn)
        logger.logger('INFO', '断开连接：%s' % conn)
        sel.unregister(conn)
        conn.close()

dic = {}
if not os.path.exists(settings.ROOT_PATH):exit("Ftp服务根目录%s不存在" % settings.ROOT_PATH)
sel = selectors.DefaultSelector()
sock = socket.socket()
sock.bind((settings.LISTEN, settings.PORT))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, server_accept)    # 新连接过来调用server_accept

while True:
    events = sel.select()   # 默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)     # key.fileobj=文件句柄


