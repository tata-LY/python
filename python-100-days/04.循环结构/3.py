#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 14:01
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm

# 输出乘法口诀表(九九表)
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d" % (j, i, j * i), end="\t")
    print()