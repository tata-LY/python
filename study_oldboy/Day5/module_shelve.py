#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# shelve 模块
# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式

import shelve
import time

z = shelve.open("shelve_test1")

name = 'LiuYang'

info = {
    'age': 26,
    'job': 'IT',
}

z['name'] = name
z['info'] = info
z['date'] = time.strftime("%Y-%m-%d")
z.close()

z = shelve.open("shelve_test1")
print(z.get("name"))
print(z.get("info"))
print(z.get("date"))