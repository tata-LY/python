#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import copy

names = ['LiuYang', 'ZhangJuan', 'LiuDongKe', 'ShuShuYuan']

print(names)
print(names[0])
print(names[0:3])
print(names[:3])
print(names[3:])
print(names[-1])

names.append('ZhangJinHua')
print(names)
names.insert(0, 'LiuYiYi')
print(names)

names[0] = 'LiuZhangYiYi'
print(names)

names.remove('ZhangJinHua')
print(names)

del names[0]
print(names)

me = names.pop(0)
print(names, me)

for i in names:
    if i == 'LiuDongKe':
        print("{name} is my father.".format(name=i))
    elif i == 'ShuShuYuan':
        print("{name} is my mother.".format(name=i))

print(names)
names.reverse()
print(names)
names.sort()
print(names)

names2 = [1, 2, 3, 4]
names.extend(names2)
print(names)
# sorted(names) # int str 不能一起排序

names2.clear()
print(names2)

print(names.index('ZhangJuan'))

names3 = names.copy()
names4 = names     # 指向同一个列表
print(names3, names4)
names.append('LiuYang')
print(names3, names4)

names.append(['dog', 'cat'])
print(names)
print(names[-1])
print(names[-1][0])

names5 = names.copy()    # 列表里的列表里的值也会跟着改动
names6 = names
names7 = copy.deepcopy(names)  # 深copy，完全独立

print(names5)
print(names6)

names[-1][0] = names[-1][0].upper()
names[0] = names[0].lower()
print(names)
print(names5)
print(names6)
print(names7)
print(names7[::2])

for index,item in enumerate(names):
    print(index,item)

str_1 = "123"
str_2 = "Abc"
str_3 = "123Abc"

print(str_1.isdigit())
print(str_2.isalpha())
print(str_3.isalnum())

