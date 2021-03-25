#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-25 9:18
# @Author  : liuyang
# @File    : common.py
# @Software: PyCharm

import re

def qq_isok(qq):
    """qq号5~11位数字,不能0开头"""
    pattern = r"^[1-9]\d{4,10}$"
    ex_qq = re.compile(pattern)
    res = ex_qq.match(qq)
    return res

def score_isok(score=''):
    flag = False
    if score.isdigit():
        score = int(score)
        if score in range(0, 101):
            flag = True
    return flag

if __name__ == '__main__':
    while True:
        qq = input(">>>")
        print(qq_isok(qq))
