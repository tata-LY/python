#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-1 11:12
# @Author  : liuyang
# @File    : 4.2_类的特性成员方法getitem.py
# @Software: PyCharm

class Foo(object):
    def __init__(self):
        self.data = {}
    def __getitem__(self, key):
        print('__getitem__', key)
        return self.data.get(key)
    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] =value
    def __delitem__(self, key):
        print('__delitem__', key)

obj = Foo()
obj['name'] = 'Alex'    # __setitem__ name Alex     # 执行__setitem__
obj['age'] = 18         # __setitem__ age 18
print(obj['name'])      # __getitem__ name\nAlex    # 执行__getitem__
print(obj.data)         # {'name': 'Alex', 'age': 18}
del obj['ssdfdf']       # __delitem__ ssdfdf    # 执行__delitem__
print(obj.data)         # {'name': 'Alex', 'age': 18}
del obj['age']          # __delitem__ age       # 执行__delitem__,实际还未删除age数据
print(obj.data)         # {'name': 'Alex', 'age': 18}