#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-20 9:30
# @Author  : liuyang
# @File    : 5.py
# @Software: PyCharm
lyrics_file = "lyrics1"
lyrics_file2 = "lyrics2"
lyrics_file3 = "lyrics3"

f = open(lyrics_file2, "rb")  # 读二进制的文件,比如网络二进制传输
print(f.read())
f.close()

#f = open(lyrics_file2, "wb")
f = open(lyrics_file2, "ab")
f.write("Hello Liuyang\n".encode())  # 二进制格式写入
f.close()