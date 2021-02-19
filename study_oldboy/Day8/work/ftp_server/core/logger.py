#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-19 10:56
# @Author  : liuyang
# @File    : logger.py
# @Software: PyCharm

from conf import settings
import os
import sys
import time

def logger(log_level, log_info):
    """日志输出"""
    log_file = settings.LOG_FILE
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())     # 当前时间
    log_info = "[ {now_time} ] {log_level} {log_info}\n".format(now_time=now_time, log_level=log_level, log_info=log_info)    # 拼接日志输出完整数据
    if not os.path.exists(log_file):
        f_w = open(log_file, "w", encoding="utf-8")
        f_w.close()
    with open(log_file, "a", encoding="utf-8") as f_a:      # 追加写入
        f_a.write(log_info)