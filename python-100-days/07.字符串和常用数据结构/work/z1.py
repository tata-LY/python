#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-11 10:44
# @Author  : liuyang
# @File    : z1.py
# @Software: PyCharm
"""
案例1：双色球选号。
"""
from random import randint

def display(balls_list):
    """
    输出列表中的双色球号码
    :param balls_list 输出的双色球列表
    :return:
    """
    print(balls_list)

def random_select():
    """
    随机选一注
    :return:
    """
    balls_list = []
    all_balls = [num for num in range(1, 36)]
    for _ in range(1, 8):
        all_balls_len = len(all_balls)
        select_ball_index = randint(1, all_balls_len)
        balls_list.append(all_balls.pop(select_ball_index))
    return balls_list


def main():
    n = int(input("机选几注："))
    for _ in range(n):
        balls_list = random_select()
        display(balls_list)

if __name__ == '__main__':
    main()