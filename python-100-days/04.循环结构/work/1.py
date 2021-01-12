#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 14:13
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

"""
练习1：输入一个正整数判断是不是素数。
1、判断输入的是一个正整数
2、素数判断依据：素数指的是只能被1和自身整除的大于1的整数。
"""
while True:
    number = int(input("请输入一个正整数: "))
    if number > 0:
        break
flag = True
for i in range(2, number):
    if number % i == 0:
        flag = False
        break
if flag == True:
    print("%d是素数。" % number)
else:
    print("%d不是素数。" % number)
