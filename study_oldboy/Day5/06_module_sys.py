#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 14:51
# @Author  : liuyang
# @File    : 06_module_sys.py
# @Software: PyCharm

import sys

# sys.argv           # 命令行参数List，第一个元素是程序本身路径
# sys.exit("Goodbye")        # 退出程序，正常退出时exit(0)
# sys.version        # 获取Python解释程序的版本信息
# sys.maxint         # 最大的Int值
# sys.path           # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       # 返回操作系统平台名称
# sys.stdout.write('please:')   # 退出时输入赋值给下面的val
# val = sys.stdin.readline()[:-1]

print(sys.argv) # 命令行参数List，第一个元素是程序本身路径    ['E:/刘洋工作/20200921/git/tata-LY/python/study_oldboy/Day5/06_module_sys.py']
# sys.exit("Goodbye")   # 退出程序，正常退出时exit(0)

print(sys.version)  # 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# print(sys.maxint)     # AttributeError: module 'sys' has no attribute 'maxint'

print(sys.path)     # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform) # win32


sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
print(val)
"""
please:ddd
ddd
"""