#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-20 9:23
# @Author  : liuyang
# @File    : 4.py
# @Software: PyCharm
lyrics_file = "lyrics1"
lyrics_file2 = "lyrics2"
lyrics_file3 = "lyrics3"

f_w = open(lyrics_file2, "w", encoding="utf-8")
f_w.write("Over\n")
f_w.flush()     # 写文件时，强制性flush到硬盘，避免数据丢失(通过python终端可以很好看到结构)
f_w.close()

f_a =  open(lyrics_file2, "a", encoding="utf-8")
f_a.seek(0)
f_a.write("Liuyang")
# f_a.truncate(10)   # 截断位置后的10个字节
f_a.close()

f = open(lyrics_file, "r+", encoding="utf-8")   # "r+" 模式是读写，光标默认在0位置，最后位置开始写
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("Over\n")
f.close()

f = open(lyrics_file2, "w+", encoding="utf-8")   # "w+" 模式是写读，先清空，再写读
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("New Over\n")
f.write("New Over\n")
f.write("New Over\n")
f.close()

f = open(lyrics_file2, "a+", encoding="utf-8")   # "a+" 模式是追加读，光标默认在最后位置
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("New Over\n")
f.close()