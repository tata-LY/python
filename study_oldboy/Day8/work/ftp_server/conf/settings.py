#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-18 14:30
# @Author  : liuyang
# @File    : settings.py
# @Software: PyCharm

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 监听
LISTEN = "0.0.0.0"

# 服务端口
PORT = 9999

# ftp server根目录
ROOT_PATH = os.path.join(BASE_DIR, 'ftproot')

# ftp用户配置文件
DB_FILE = os.path.join(BASE_DIR, 'db/user.conf' )

# 日志文件
LOG_FILE = os.path.join(BASE_DIR, 'logs/ftp.log' )

# 默认用户配额
DEFAULT_MAX_SIZE = 10240000000
