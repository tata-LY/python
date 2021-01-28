#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 13:54
# @Author  : liuyang
# @File    : 04_module_random.py
# @Software: PyCharm

import random
import string

print(random.random())  # 0-1   # 0.2007391524410863
print(random.randint(1,10)) # 1-10 int  # 2
print(random.randrange(3)) # 0-2    # 2
print(random.randrange(1,3)) # 1-2  # 2
print(random.choice("abcdefg")) # 字符串中选择一个  # f
print(random.sample("abcdefg",3)) # 随机3三个['e', 'c', 'g']
print(random.choice([1,2,3,4,5,6,7,8])) # 列表中随机一个
print(random.uniform(1,10)) # 1-10 float    # 7.221045498866636

l = [1,2,3,4,5,6,7,8]
random.shuffle(l)  # 打乱顺序
print(l)    # [2, 8, 1, 6, 4, 7, 3, 5]

# 生产随机验证码
check_code = ''
for i in range(5):
    current = random.randrange(0,5)
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = str(random.randint(0,9))
    check_code += str(tmp)

print(check_code)   # P22U1


# 补充下string模块来进行随机验证码功能
print(string.digits)  # 输出包含数字0~9的字符串   0123456789
print(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # 包含所有小写字母的字符串   abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # 包含所有大写字母的字符串   ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(random.choice(string.digits))     # 0-9随机一个
print(random.choice(string.ascii_letters))  # 随机一个字母