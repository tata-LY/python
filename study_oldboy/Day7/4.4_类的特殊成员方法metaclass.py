#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 13:49
# @Author  : liuyang
# @File    : 4.4_类的特殊成员方法metaclass.py
# @Software: PyCharm

"""类实例化时，先调用__call__，然后__call__调用__new__，__new__调用__init__"""

class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        print("--MyType init---")
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        """实例化，先调用__call__，__call__调用__new__"""
        print("--MyType call---")

        obj = self.__new__(self, *args, **kwargs) # 调用Foo的__new__
        obj.data = {"name":111}
        self.__init__(obj, *args, **kwargs)     # 调用Foo的__init__

class Foo(object):
    __metaclass__ = MyType  # 在python2中会先执行MyType里的__init__、__call__

    def __init__(self, name):
        self.name = name
        print("Foo ---init__")

    def __new__(cls, *args, **kwargs):
        """__new__实例化,__new__调用__init__"""
        print("Foo --new--")
        print(object.__new__(cls))      # <__main__.Foo object at 0x00000162352E09D0>
        return object.__new__(cls)      # 继承父亲的__new__方法



# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo("Alex")
print(obj.name)     # Alex
