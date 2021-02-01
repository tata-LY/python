#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 13:29
# @Author  : liuyang
# @File    : 4.3_类的特殊成员方法__new__.py
# @Software: PyCharm

class Foo(object):
    def __init__(self, name):
        self.name = name

f =  Foo('Docker Liu')
print(type(f))      # <class '__main__.Foo'>
print(type(Foo))    # <class 'type'>


def func(self):
    print('name:%s age:%s' % (self.name, self.age))

def __init__(self , name, age):
    self.name = name
    self.age = age

Foo = type('Foo', (), {'talk' : func, '__init__' : __init__})  # Foo就成了一个类对象,type就是类的类。

f = Foo('DockerLiu', 29)
f.talk()            # name:DockerLiu age:29
print(type(Foo))    # <class 'type'>