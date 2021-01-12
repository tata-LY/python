#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-7 10:00
# @Author  : liuyang
# @File    : 2.py
# @Software: PyCharm

"""使用列表"""
list1 = [1, 3, 5, 7, 100]
print(list1)
list2 = ['hello', 'world'] * 3
print(list2)
print(len(list2))
print(list1[0])
print(list1[-1])
list1[-2] = 9
print(list1)
for index in range(len(list1)):
    print(list1[index], end=',')
for elem in list1:
    print(elem)
for index, elem in enumerate(list1):
    print(index, elem)

list1.append(1000)
print(list1)
list1.insert(3, 7) # 插入
print(list1)
list1.extend([10000, 100000])
print(list1)
list1 += [-1, -3]
print(list1)
# list1.remove(-2) # 不存在，异常
list1.remove(-3)
print(list1)
list1.pop(-2) # 按位置删除
list1.pop(-1)
print(list1)
del list1[-1]
print(list1)
list1.clear()
print(list1)

family = ['ly', 'zj']
family += ['ldk', 'ssy']
print(family)
print(family[0:2])
print(family[::-1])
family.append('zjh')
family.append('rll')
print(sorted(family)) # sorted函数返回列表排序后的拷贝不会修改传入的列表
print(sorted(family, reverse=True)) # 倒序
print(sorted(family, key=len)) # 长度排序

print(family)
family.sort(reverse=True) # 直接给列表排序(倒序)
print(family)