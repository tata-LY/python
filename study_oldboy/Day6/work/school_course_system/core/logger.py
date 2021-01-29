#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from conf import settings
import os
import sys
import time

def logger(log_type, log_info):
    """日志输出"""
    log_file = '%s/logs/%s' % (settings.BASE_DIR, settings.LOGS_TYPES[log_type])    # 根据log_type拼接日志文件绝对路径
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())     # 当前时间
    log_info = "[ {now_time} ] {log_level} {log_info}\n".format(now_time=now_time, log_level=settings.LOGS_LEVEL, log_info=log_info)    # 拼接日志输出完整数据
    if not os.path.exists(log_file):
        f_w = open(log_file, "w", encoding="utf-8")
        f_w.close()
    with open(log_file, "a", encoding="utf-8") as f_a:      # 追加写入
        f_a.write(log_info)