#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# json & pickle 模块
# 用于序列化的两个模块
#
# json，用于字符串 和 python数据类型间进行转换
# pickle，用于python特有的类型 和 python的数据类型间进行转换
# Json模块提供了四个功能：dumps、dump、loads、load
#
# pickle模块提供了四个功能：dumps、dump、loads、load

import json
import pickle

data = {
    'A': "a",
    "B": "b",
}
print(data, type(data))
data_json = json.dumps(data)
print(data_json, type(data_json))
print(json.loads(data_json), type(json.loads(data_json)))

data_pickle = pickle.dumps(data)
print(data_pickle, type(data_pickle))
print(pickle.loads(data_pickle), type(pickle.loads(data_pickle)))