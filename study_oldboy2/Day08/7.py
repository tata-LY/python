#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-20 9:43
# @Author  : liuyang
# @File    : 7.py
# @Software: PyCharm

lyrics_file = "lyrics1"
lyrics_file2 = "lyrics2"
lyrics_file3 = "lyrics3"

# 使用with语句操作文件，自动close
with open(lyrics_file, 'r', encoding='utf-8') as f_r:
    for line in f_r.readlines():
        print(line, end='')

with open(lyrics_file3, 'a', encoding='utf-8') as f_a:
    f_a.write('with open\n')