#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-26 10:13
# @Author  : liuyang
# @File    : 15_pickle.py
# @Software: PyCharm

import pickle

def sayhi(name):
    print("hello %s" % name)

info = {
    'name': "Liuyang",
    'age': 12,
    'func': sayhi
}

file = 'pickle.txt'

with open(file, "wb") as f_w:
    # print(json.dumps(info))
    # f_w.write(str(info))
    f_w.write(pickle.dumps(info))

with open(file, "rb") as f_r:
    data = pickle.loads(f_r.read())

print(type(data))       # <class 'dict'>
print(data)     # {'name': 'Liuyang', 'age': 12, 'func': <function sayhi at 0x000002985F545310>}
data['func']('Liuyang')      # hello Liuyang
