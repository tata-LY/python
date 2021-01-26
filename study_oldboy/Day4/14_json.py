#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-26 10:11
# @Author  : liuyang
# @File    : 14_json.py
# @Software: PyCharm

import json

info = {
    'name': "Liuyang",
    'age': 12,
    'sex': 'M',

}

file = 'json.txt'

with open(file, "w", encoding="utf-8") as f_w:
    # print(json.dumps(info))
    # f_w.write(str(info))
    f_w.write(json.dumps(info))

with open(file, "r", encoding="utf-8") as f_r:
    data = json.loads(f_r.read())

print(type(data))   # <class 'dict'>
print(data)     # {'name': 'Liuyang', 'age': 12, 'sex': 'M'}
