#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-18 8:49
# @Author  : liuyang
# @File    : 4.py
# @Software: PyCharm

exit_flag = False

for i in range(10):
    if i <5:
        continue  # 结束本次循环，继续下一次循环
    print(i )
    for j in range(10):
        print("layer2",j)
        if j == 6:
            exit_flag = True
            break
    if exit_flag:
        break