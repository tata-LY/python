#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-20 9:10
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm

lyrics_file = "lyrics1"
lyrics_file2 = "lyrics2"
lyrics_file3 = "lyrics3"

# 显示前五行
f_r = open(lyrics_file, "r", encoding="utf-8")
for i in range(5):
    print(f_r.readline(), end='')  # 文件内容本来就有换行
f_r.close()

# readlines 读取文件存放在内存里，适合小文件
f_r = open(lyrics_file, "r", encoding="utf-8")
# print(f_r.readlines())   # list格式，这里获取后，下面再获取就是[]
for line in f_r.readlines():
    print(line.rstrip())
f_r.close()

f_r = open(lyrics_file, "r", encoding="utf-8")
print("-".center(30, "-"))
for index,item in enumerate(f_r.readlines()):
    print(index,item.rstrip())
f_r.close()

# 一行行读，内存里只存一行的值,自己加个变量自增来记录行数
count = 0
f_r = open(lyrics_file, "r", encoding="utf-8")
for line in f_r:
    count += 1
    print(count, line.rstrip())
f_r.close()