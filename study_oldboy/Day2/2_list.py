#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import copy

names = ['LiuYang', 'ZhangJuan', 'LiuDongKe', 'ShuShuYuan']

print(names)        # ['LiuYang', 'ZhangJuan', 'LiuDongKe', 'ShuShuYuan']
print(names[0])     # LiuYang
print(names[0:3])   # ['LiuYang', 'ZhangJuan', 'LiuDongKe']
print(names[:3])    # ['LiuYang', 'ZhangJuan', 'LiuDongKe']
print(names[3:])    # ['ShuShuYuan']
print(names[-1])    # ShuShuYuan

names.append('ZhangJinHua')
print(names)        # ['LiuYang', 'ZhangJuan', 'LiuDongKe', 'ShuShuYuan', 'ZhangJinHua']
names.insert(0, 'LiuYiYi')
print(names)        # ['LiuYiYi', 'LiuYang', 'ZhangJuan', 'LiuDongKe', 'ShuShuYuan', 'ZhangJinHua']

names[0] = 'LiuZhangYiYi'
print(names)        # ['LiuZhangYiYi', 'LiuYang', 'ZhangJuan', 'LiuDongKe', 'ShuShuYuan', 'ZhangJinHua']

names.remove('ZhangJinHua')
print(names)        # ['LiuZhangYiYi', 'LiuYang', 'ZhangJuan', 'LiuDongKe', 'ShuShuYuan', 'ZhangJinHua']

del names[0]
print(names)        # ['LiuYang', 'ZhangJuan', 'LiuDongKe', 'ShuShuYuan']

me = names.pop(0)
print(names, me)    # ['ZhangJuan', 'LiuDongKe', 'ShuShuYuan'] LiuYang

for i in names:
    if i == 'LiuDongKe':
        print("{name} is my father.".format(name=i))        # LiuDongKe is my father.
    elif i == 'ShuShuYuan':
        print("{name} is my mother.".format(name=i))        # ShuShuYuan is my mother.

print(names)        # ['ZhangJuan', 'LiuDongKe', 'ShuShuYuan']
names.reverse()
print(names)        # ['ShuShuYuan', 'LiuDongKe', 'ZhangJuan']
names.sort()
print(names)        # ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan']

names2 = [1, 2, 3, 4]
names.extend(names2)
print(names)        # ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4]
# sorted(names) # int str 不能一起排序

names2.clear()
print(names2)       # []

print(names.index('ZhangJuan'))     # 2

names3 = names.copy()
names4 = names     # 指向同一个列表
print(names3, names4)       # ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4] ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4]
names.append('LiuYang')     # ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4] ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4, 'LiuYang']
print(names3, names4)       # ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4, 'LiuYang', ['dog', 'cat']]

names.append(['dog', 'cat'])
print(names)            # ['dog', 'cat']
print(names[-1])        # dog
print(names[-1][0])     #

names5 = names.copy()    # 列表里的列表里的值也会跟着改动
names6 = names
names7 = copy.deepcopy(names)  # 深copy，完全独立

print(names5)       # ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4, 'LiuYang', ['dog', 'cat']]
print(names6)       # ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4, 'LiuYang', ['dog', 'cat']]

names[-1][0] = names[-1][0].upper()
names[0] = names[0].lower()
print(names)            # ['liudongke', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4, 'LiuYang', ['DOG', 'cat']]
print(names5)           # ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4, 'LiuYang', ['DOG', 'cat']]
print(names6)           # ['liudongke', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4, 'LiuYang', ['DOG', 'cat']]
print(names7)           # ['LiuDongKe', 'ShuShuYuan', 'ZhangJuan', 1, 2, 3, 4, 'LiuYang', ['dog', 'cat']]
print(names7[::2])      # ['LiuDongKe', 'ZhangJuan', 2, 4, ['dog', 'cat']]

for index,item in enumerate(names):
    print(index,item)
"""
0 liudongke
1 ShuShuYuan
2 ZhangJuan
3 1
4 2
5 3
6 4
7 LiuYang
8 ['DOG', 'cat']
"""
str_1 = "123"
str_2 = "Abc"
str_3 = "123Abc"

print(str_1.isdigit())  # True
print(str_2.isalpha())  # True
print(str_3.isalnum())  # True
