#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-29 14:32
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm

"""
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
1、判断输入的是一个正整数
2、最大公约数：两个数的最大公约数是两个数的公共因子中最大的那个数
3、最小公倍数：两个数的最小公倍数则是能够同时被两个数整除的最小的那个数,x*y/最大公约数
"""
while True:
    number1 = int(input("请输入第一个一个正整数: "))
    if number1 > 0:
        break
while True:
    number2 = int(input("请输入第一个一个正整数: "))
    if number2 > 0:
        break

if number2 > number1:
    number1, number2 = number2, number1

for i in range(number1, 0, -1):
    if number1 % i == 0 and number2 % i == 0:
        print("%d和%d的最大公约数是%d" % (number1, number2, i))
        print("%d和%d的最小公倍数是%d" % (number1, number2, number1 * number2 // i))
        break
