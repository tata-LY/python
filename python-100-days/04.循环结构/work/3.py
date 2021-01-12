#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 14:46
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm
"""
练习3：打印如下所示的三角形图案。
*
**
***
****
*****
    *
   **
  ***
 ****
*****
    *
   ***
  *****
 *******
*********
"""

for i in range(1, 10):
    for j in range(1, i+1):
        print("*", end='')
    print()

print('---------------------------')

for i in range(1, 10):
    for j in range(9, 0, -1):
        if i >= j:
            print("*", end='')
        else:
            print(" ", end='')
    print()


for i in range(1, 6):
    print("{:^9}".format('*'*(2*i-1)))