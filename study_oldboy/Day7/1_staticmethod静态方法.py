#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 9:37
# @Author  : liuyang
# @File    : 1.静态方法.py
# @Software: PyCharm

class Dog(object):

    def __init__(self, name):
        self.name = name

    @ staticmethod  # 只是类里面的一个函数，实际上跟类没什么关系了
    def eat(self):
        print("%s is eating %s" % (self.name, '包子'))

    def talk(self):
        print('%s is talking' % self.name)

d = Dog("ZhangJuan")
d.eat(d)        # ZhangJuan is eating 包子
d.talk()        # ZhangJuan is talking