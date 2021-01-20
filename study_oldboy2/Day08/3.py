#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-20 9:18
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm
lyrics_file = "lyrics1"
lyrics_file2 = "lyrics2"
lyrics_file3 = "lyrics3"

# 文件读取位置
f_r = open(lyrics_file, "r", encoding="utf-8")
print(f_r.tell())
print(f_r.read(5))
print(f_r.readline(), end='')
print(f_r.tell())
print(f_r.seekable()) # 是否可以移动
f_r.seek(0)   # 位置移到文件最开始的地方
print(f_r.readline(), end='')
print(f_r.encoding)   # 文件编码
print(f_r.name)  # 文件名字
f_r.close()