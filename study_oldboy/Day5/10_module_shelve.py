#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 15:43
# @Author  : liuyang
# @File    : 10_module_shelve.py
# @Software: PyCharm

# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式

import shelve
import time

def sayhi(name):
    print("hello %s" % name)

z = shelve.open("10_shelve_test1")  # 打开一个文件
name = 'LiuYang'
info = {
    'age': 29,
    'job': 'IT',
}

z['name'] = name
z['info'] = info
z['date'] = time.strftime("%Y-%m-%d")
z['sayhi'] = sayhi  # 存入函数
z.close()

z = shelve.open("10_shelve_test1")  # 打开一个文件
print(z.get("name"))
print(z.get("info"))
print(z.get("date"))
z.get('sayhi')('Liuyang')   # 调用函数
