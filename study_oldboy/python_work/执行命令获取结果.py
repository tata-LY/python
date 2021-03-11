#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-11 10:41
# @Author  : liuyang
# @File    : 执行命令获取结果.py
# @Software: PyCharm

"""
不分系统，执行命令。并打印命令执行结果
"""

import subprocess
import chardet

while True:
    cmd = input(">>>").strip()
    res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
    out=res.stdout.readlines()
    err=res.stderr.readlines()
    cmd_result_b = out if out else err
    cmd_result = b''
    for line in cmd_result_b:
        cmd_result += line
    # print(cmd_result)
    encoding = chardet.detect(cmd_result)['encoding']       # 获取二进制格式的字符编码
    # print(encoding)
    print(cmd_result.decode(encoding))