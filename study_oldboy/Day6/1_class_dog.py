#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-28 14:58
# @Author  : liuyang
# @File    : 1_class_dog.py
# @Software: PyCharm

class Dog:
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print('%s: wang wang wang!' % self.name)

d1 = Dog('Dog1')
d2 = Dog('Dog2')
d3 = Dog('Dog3')

d1.bulk()
d2.bulk()
d3.bulk()