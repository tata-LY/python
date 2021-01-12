#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-6 13:47
# @Author  : liuyang
# @File    : 4.py
# @Software: PyCharm
"""
练习4：写一个程序判断输入的正整数是不是回文素数。
"""

def is_palindrome(num):
    temp = num
    total = 0
    while num > 0:
        total = total * 10 + num % 10
        num //= 10
    return total == temp

if __name__ == '__main__':
    num = int(input("输入一个正整数："))
    if is_palindrome(num):
        print("输入的数是回文数！")
    else:
        print("输入的数不是回文数！")