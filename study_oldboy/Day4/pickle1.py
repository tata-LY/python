#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import pickle

def sayhi():
    print("hello world")

info = {
    'name': "Liuyang",
    'age': 12,
    'func': sayhi
}

with open("test2.txt", "wb") as f_w:
    # print(json.dumps(info))
    # f_w.write(str(info))
    f_w.write(pickle.dumps(info))

with open("test2.txt", "rb") as f_r:
    data = pickle.loads(f_r.read())

print(data)
print(data['func']())