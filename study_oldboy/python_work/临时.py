#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-19 9:50
# @Author  : liuyang
# @File    : 临时.py
# @Software: PyCharm


# import sys
# import subprocess
# import chardet
#
# while True:
#         cmd = input(">>>").strip()
#         p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
#         out,err = p.communicate()
#         # print(out)
#         print(err)
#         # encoding = chardet.detect(out)['encoding']
#         # print(encoding)
#         # out = out.decode(encoding)
#         # for line in out.splitlines():
#         #     print(line)

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


