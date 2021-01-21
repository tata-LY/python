#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-15 15:19
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

import random

num = random.randint(1, 100)
print('猜数字游戏开始'.center(30, '*'))
count = 1
guess_num = int(input("猜数："))
while True:
    if guess_num < num:
        guess_num = int(input("太小了："))
    elif guess_num > num:
        guess_num = int(input("太大了："))
    elif guess_num == num:
        exit("恭喜在第%d次猜对了数字%d" %  (count,num))
    count += 1
