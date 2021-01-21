#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-19 16:19
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm

# README
# UNICODE 默认英文和中文都是两个字节
# ASCII 只支持英文和特许字符
# UTF-8 一个中文3个字节

import sys

print(sys.getdefaultencoding())

'''
# python2 版本可以如下转换

# s = u"你好"  可以这样定义
s = "你好"
s_to_unicode = s.decode("utf-8")
s_to_gbk = s_to_unicode.encode("gbk")
s_to_utf8 = s_to_unicode.encode("utf-8")
print(s_to_unicode)
print(s_to_gbk)
print(s_to_utf8)
'''

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

s = '特斯拉'
s_utf8 = s.encode('UTF-8')
s_gbk = s.encode('GBK')
print(s, s.encode(), s_utf8, str_gbk) # python3 默认是UTF-8
print(s, s_utf8.decode(), s_gbk.decode('GBK', 'strict'))
# 因为decode的函数原型是decode([encoding], [errors='strict'])，可以用第二个参数控制错误处理的策略，默认的参数就是strict，代表遇到非法字符时抛出异常； 如果设置为ignore，则会忽略非法字符； 如果设置为replace，则会用?取代非法字符； 如果设置为xmlcharrefreplace，则使用XML的字符引用。