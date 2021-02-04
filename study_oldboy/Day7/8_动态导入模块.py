#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-3 13:38
# @Author  : liuyang
# @File    : 8_动态导入模块.py
# @Software: PyCharm

import lib.aa
obj = lib.aa.C()
obj(1, 2, 3 , a=4, b=5)     # runing call (1, 2, 3) {'a': 4, 'b': 5}

modname = "lib.aa"
"""importlib 官方建议用这个"""
import importlib
aa = importlib.import_module(modname)
obj = aa.C()
obj(1, 2, 3 , a=4, b=5)     # runing call (1, 2, 3) {'a': 4, 'b': 5}

"""__import__"""
lib = __import__(modname)   # lib
print(lib)      # <module 'lib' from 'E:\\刘洋工作\\20200921\\git\\tata-LY\\python\\study_oldboy\\Day7\\lib\\__init__.py'>
obj = getattr(lib.aa, "C")()    # import lib.aa, obj = lib.aa.C()
obj(1, 2, 3 , a=4, b=5)     # runing call (1, 2, 3) {'a': 4, 'b': 5}


