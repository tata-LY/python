#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-15 10:43
# @Author  : liuyang
# @File    : 5.py
# @Software: PyCharm

score = int(input("score:"))


if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 50:
    print("D")
else:
    print("滚")