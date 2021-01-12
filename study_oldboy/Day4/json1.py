#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import json


info = {
    'name': "Liuyang",
    'age': 12
}

with open("test1.txt", "w", encoding="utf-8") as f_w:
    # print(json.dumps(info))
    # f_w.write(str(info))
    f_w.write(json.dumps(info))

with open("test1.txt", "r", encoding="utf-8") as f_r:
    data = json.loads(f_r.read())

print(data)