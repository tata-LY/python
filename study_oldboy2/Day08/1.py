#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-20 8:58
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm


lyrics_file = "lyrics1"
lyrics_file2 = "lyrics2"
lyrics_file3 = "lyrics3"

f_r = open(lyrics_file, encoding="utf-8")  # 文件句柄  默认为 "r" 模式,只读
print(f_r)
data = f_r.read()    # 一个string赋值给data
data2 = f_r.read()   # 读取不到了
f_r.close()
print('data的值：\n%s' % data)
print('data2的值：%s' % data2)
print(type(data))    # string

f_w = open(lyrics_file2, "w", encoding="utf-8")   # "w" 模式是覆盖,不能读
f_w.write("Over\n")
f_w.close()

f_a = open(lyrics_file2, "a", encoding="utf-8")     # "a" 模式是追加，不能读
f_a.write("Over")
f_a.close()



