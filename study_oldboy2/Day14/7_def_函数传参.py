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

# 默认参数特点：调用函数的时候，默认参数非必须传递
def conn(host,port=3306):
    print(host, port)

conn(host='10.10.10.1')
conn(host='10.10.10.2', port=33060)
