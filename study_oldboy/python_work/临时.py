#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-19 9:50
# @Author  : liuyang
# @File    : 临时.py
# @Software: PyCharm


list = [10, 12, 33, 0, 2, 3, 5, 4, 9, 6]

list_len = len(list)

for i in range(list_len):
    for j in range(i+1, list_len):
        if list[j] < list[i]:
            list[i], list[j] = list[j], list[i]

    print(list)