#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 15:02
# @Author  : liuyang
# @File    : 6_异常处理.py
# @Software: PyCharm

def bulk(self):
    print("%s is yelling...." % self.name)

class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))

names = ['Liu', 'Zhang']
data = {}

try:
    open('1111.txt')
except Exception as e:      # 抓取所有的错误
    print("错误：%s" % e)  # 错误：[Errno 2] No such file or directory: '1111.txt'

try:
    # names[3]
    # data['name']
    open('111.txt')
except (KeyError,IndexError) as e:     # 同时抓取两种错误
    print("错误：%s" % e)
except IndexError as e:
    print("字典data里没有%s这个key" % e)
except BaseException as e:  # 所有异常基类
    print("未知错误: %s" % e)
else:
    print("一切正常")
finally:
    print("不管有没有错，最后都会执行")
