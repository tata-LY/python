#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-27 17:06
# @Author  : liuyang
# @File    : 14.2_module_hmac.py
# @Software: PyCharm

import hmac
h = hmac.new(b'liu', b"yang")
h.update(b'hellowo')
print(h.digest())
print(h.hexdigest())  # 十六进制

h2 = hmac.new("刘洋".encode(encoding="utf-9"))
print(h2.hexdigest())
