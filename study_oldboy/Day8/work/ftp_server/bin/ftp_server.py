#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-18 14:19
# @Author  : liuyang
# @File    : ftp_server.py
# @Software: PyCharm

import os
import sys
import socketserver


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import main
from conf import settings


if __name__ == "__main__":
    if not os.path.exists(settings.ROOT_PATH):exit("Ftp服务根目录%s不存在" % settings.ROOT_PATH)
    print("FTP server staring...", settings.ROOT_PATH, settings.LISTEN, settings.PORT)
    server = socketserver.ThreadingTCPServer((settings.LISTEN, settings.PORT), main.MyTCPHandler)    # 多线程
    server.serve_forever()