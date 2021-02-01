#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 10:02
# @Author  : liuyang
# @File    : 3.1_property属性方法.py
# @Software: PyCharm

class Dog(object):
    """这个类描述狗这个对象"""
    def __init__(self, name):
        self.name = name
        self.__food = None      # 先定义self.__food

    @ property # attribute
    def eat(self,):
        print("%s is eating %s" % (self.name, self.__food))
    @eat.setter
    def eat(self, food):
        print("set to food:%s" % food)
        self.__food = food      # self.__food 赋值
    @eat.deleter
    def eat(self):
        del self.__food         # 删除self.__food
        print("self.__food删除了")

    def talk(self):
        print('%s is talking' % self.name)

    def __call__(self, *args, **kwargs):
        print("runing call", args, kwargs)

    def __str__(self):
        return "<obj:%s>" % self.name

d = Dog("Alex")
d.eat       # Alex is eating None
d.eat='baozi'   # set to food:baozi     # @eat.setter赋值self.__food='bapzi'
d.eat       # Alex is eating baozi
del d.eat       # self.__food删除了    # @eat.deleter删除self.__food
d(1, 2, 3, name = 'Liuyang')   # runing call (1, 2, 3) {'name': 'Liuyang'}    # 调用__call__

print(Dog.__dict__)
"""
打印类里面的所有属性，不包括实例属性
{'__module__': '__main__', '__doc__': '这个类描述狗这个对象', '__init__': <function Dog.__init__ at 0x0000016DFF3ED820>, 'eat': <property object at 0x0000016DFF348360>, 'talk': <function Dog.talk at 0x0000016DFF5A9B80>, '__call__': <function Dog.__call__ at 0x0000016DFF5AA1F0>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>}
"""
print(d.__dict__)   # {'name': 'Alex'}

print(d)    # <obj:Alex>