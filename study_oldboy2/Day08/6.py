#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-20 9:33
# @Author  : liuyang
# @File    : 6.py
# @Software: PyCharm
lyrics_file = "lyrics1"
lyrics_file2 = "lyrics2"
lyrics_file3 = "lyrics3"

f_r = open(lyrics_file, "r", encoding="utf-8")
f_w = open(lyrics_file3, "w", encoding="utf-8")
for line in f_r:
    if line == "So much I need to say\n":
        line = line.replace("I", "liuyang")
        f_w.write(line.upper())
    else:
        f_w.write(line)
f_r.close()
f_w.close()