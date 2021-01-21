#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 15:03
# @Author  : liuyang
# @File    : 7_def_函数传参.py
# @Software: PyCharm

def test(x,y,z):
    print(x, y, z)

test(z=3, y=2,x=1) # 与形参顺序无关
test(1, 2, 3)  # 与形参一一对应
test(1, z=3, y=2)
