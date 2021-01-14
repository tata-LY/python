#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-13 17:04
# @Author  : liuyang
# @File    : read_file.py
# @Software: PyCharm

"""
file 里保存压缩文件名以及解压密码（有密码或无密码），数据格式如下类型：
01.KGOB2.8.30(R)_U集中交易现金宝迁移升级包   解压密码：hq2wDS5k
02.KGOB2.8.30(R)_安信证券_01U集中交易一卡多签升级包 解压密码：无
03.KGOB2.8.30(R)_安信证券_02U集中交易上海定向可转债&科创板可转债&上海债券非交易平台迁移升级包
"""

file = 'conf.txt'
regex_str = "解压密码："
file_passwd = {}

f_r = open(file, "r", encoding="utf-8")
# print(f_r.readlines())
for line in f_r.readlines():
    file_name = line.strip().split(regex_str)[0].strip()
    if regex_str in line:
        passwd = line.strip().split(regex_str)[-1]
        if passwd != '无':
            file_passwd[file_name] = passwd
        else:
            file_passwd[file_name] = ''
    else:
        file_passwd[file_name] = ''

f_r.close()

print(file_passwd)