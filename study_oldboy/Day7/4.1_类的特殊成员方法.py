#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 10:50
# @Author  : liuyang
# @File    : 4_index.py
# @Software: PyCharm

from lib.aa import C

obj = C()
print(obj.__module__)   # lib.aa    # 输出模块
print(obj.__class__)    # <class 'lib.aa.C'>    # 输出类
obj(1, 2, 3, name = 'Liuyang')   # runing call (1, 2, 3) {'name': 'Liuyang'}    # 调用__call__

print(C.__dict__)
"""
打印类里面的所有属性，不包括实例属性
{'__module__': 'lib.aa', '__init__': <function C.__init__ at 0x00000167F783D8B0>, '__call__': <function C.__call__ at 0x00000167F783DA60>, '__dict__': <attribute '__dict__' of 'C' objects>, '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None}
"""

print(obj.__dict__)     # {'name': 'Alex'}  # 打印所有实例属性，不包括类属性
print(obj)  # <obj:Alex>    # __str__