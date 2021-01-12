#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 16:54
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm

# 实现将一个正整数反转，例如：将12345变成54321
# 从低位数开始取，往高位数每取一位，新的数就*10。
while True:
    num = int(input("请输入一个正整数："))
    if num > 0:
        break
re_num = 0
while num != 0:
    re_num = re_num * 10 + num % 10
    num //= 10
print(re_num)