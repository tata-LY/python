#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

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