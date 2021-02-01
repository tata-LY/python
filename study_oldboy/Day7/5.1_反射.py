#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 14:18
# @Author  : liuyang
# @File    : 5.1_反射.py
# @Software: PyCharm

def bulk(self):
    print("%s is yelling...." % self.name)

class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))

d = Dog('NiuHanYang')
choice = input(">>>").strip()

if hasattr(d, choice):  # hasattr判断类实例化d中是否有choice这个方法（eat）
    getattr(d, choice)('包子')    # NiuHanYang is eating 包子 # getattr执行类实例化d中choice方法（eat）
    setattr(d, 'name', "ChenRongHua")   # 修改self.name = 'ChenRongHua'
    print(getattr(d, 'name'))       # ChenRongHua
    print(d.name)       # ChenRongHua
    getattr(d, choice)('包子')    # ChenRongHua is eating 包子
    delattr(d, 'name')  # 删除self.name
    # print(d.name)     # AttributeError: 'Dog' object has no attribute 'name'
else:
    print("%s方法不存在，现在构建..." % choice)
    setattr(d, choice, bulk)
    # d.talk(d) # choice='talk',和下面getattr(d, choice)(d)调用一样
    getattr(d, choice)(d)   # NiuHanYang is yelling....

    setattr(d, choice, 22)
    print(getattr(d, choice))   # 22



