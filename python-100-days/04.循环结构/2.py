#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 13:43
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm

"""
while
猜数字游戏: 计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
"""

import random
answer = random.randint(1, 100)
counter = 0
while True:
    counter +=1
    number = int(input("请输入你猜的数字[1-100]："))
    if number > answer:
        print("小一点！")
    elif number < answer:
        print("大一点！")
    elif number == answer:
        print("您总共猜了%d次,恭喜猜对了！" % counter)
        break