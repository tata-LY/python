#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 16:44
# @Author  : liuyang
# @File    : 14.1_module_hashlib.py
# @Software: PyCharm

import hashlib

# md5 不能反解
m = hashlib.md5()
m.update(b"hello")
print(m.digest())   # b']A@*\xbcK*v\xb9q\x9d\x91\x10\x17\xc5\x92'
print(m.hexdigest())    # 5d41402abc4b2a76b9719d911017c592  # 16进制

m.update(b"It's me")
print(m.digest())   # b"d\xf6\x9d\x95\x13[\xc1=H'\xf8q\xb3\x7fx\x0f"
print(m.hexdigest())    # 64f69d95135bc13d4827f871b37f780f

m2 = hashlib.md5()
m2.update(b"helloIt's me")  # 等于上面两次update拼接
print(m2.digest())  # b"d\xf6\x9d\x95\x13[\xc1=H'\xf8q\xb3\x7fx\x0f"
print(m2.hexdigest())   # 64f69d95135bc13d4827f871b37f780f

# sha1
s1 = hashlib.sha1()
s1.update(b"helloIt's me")
print(s1.hexdigest())   # 499cae7df71137c382efff67c03b1c936b4cc4ff