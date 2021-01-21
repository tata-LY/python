#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-19 8:24
# @Author  : liuyang
# @File    : 3.py
# @Software: PyCharm

"""使用字符串"""

s1 = 'hello, world!'
s2 = "hello, world!"
s3 = """
hello,
world!
"""
print(s1, s2, s3)

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a87\u661a'
print(s1, s2)

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2)

s1 = 'hello ' * 3
print(s1) # hello hello hello
s2 = s1 + 'world'
print(s2)
print('hello' in s2)
print(s1 in s2)

str = 'abcd1234'
print(str[2])
print(str[2:5])
print(str[2:])
print(str[2::2])
print(str[::2])
print(str[::-1])
print(str[::-2])
print(str[-3:-1])
print(str[-3::-1])

print(len(str))
print(len('刘洋'))
print('刘洋'[1])

# 获得字符串首字母大写的拷贝
print('liuyang'.capitalize())
# 获得字符串每个单词首字母大写的拷贝
print('hello world!'.title())

print('hello world'.upper()) # 全大写
print('Hello World'.lower()) # 全小写
print('helloworld'.find('l')) # 第一个串位置
print('hello world'.find('Hello')) # 找不到为-1

print('hello world'.index('l'))
# print('hello.world'.index('Hello')) # 找不到会异常
str1 = 'Hello ABCabc'
print(str1.startswith('Hello')) # 检查字符串是否以指定的字符串开头
print(str1.startswith('hello'))

print(str1.endswith('abc')) # 检查字符串是否以指定的字符串结尾
print(str1.endswith('ABC'))

print(str1.center(50, '*')) # 将字符串以指定的宽度居中并在两侧填充指定的字符
for i in range(1, 6):
    str = '*' * (2 * i - 1)
    print(str.center(9, ' '))
print(str1.rjust(50, "*"))
print(str1.ljust(50, '*'))
str2 = '123456'
print(str2.isdigit()) # 判断字符串是否由纯数字组成
print(str2.isalpha())
print(str1.isalnum()) # 判断字符串是否由数字和字母组成
print('abc123'.isalnum())

str3 = '  ainiyang20@qq.com  '
print(str3)
print(str3.strip()) # 删除左右两侧空格

a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print('{a} * {b} = {c}'.format(a = a, b = b, c = a * b))
print(f'{a} * {b} = {a * b}')