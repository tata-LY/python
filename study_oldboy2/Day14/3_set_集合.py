#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-21 14:05
# @Author  : liuyang
# @File    : 3_set_集合.py
# @Software: PyCharm

"""
集合
- 去重，把一个列表变成集合，就自动去重了
- 关系测试，测试两组数据之前的交集、差集、并集等关系
"""

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)

list_2 =set([2,6,0,66,22,8,4])
print('集合'.center(30, '*'))
print(list_1,list_2)

#交集
print('交集'.center(30, '*'))
print(  list_1.intersection(list_2) )
print(list_1 & list_2)

#并集
print('并集'.center(30, '*'))
print(list_1.union(list_2))
print(list_2 | list_1)

#差集 in list_1 but not in list_2
print('差集'.center(30, '*'))
print(list_1.difference(list_2))    # difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
print(list_1 - list_2) # in list 1 but not in list 2
print(list_2.difference(list_1))

#子集
print('子集'.center(30, '*'))
list_3 = set([1,3,7])
print(list_3.issubset(list_1))  # issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False
print(list_1.issuperset(list_3)) # issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。


#对称差集
print('对称差集'.center(30, '*'))
print(list_1.symmetric_difference(list_2)) # symmetric_difference() 方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
print(list_1 ^ list_2)

# 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
list_4 = set([5,6,7,8])
print('是否有相同的元素'.center(30, '*'))
print(list_3.isdisjoint(list_4)) # Return True if two sets have a null intersection.

# 给集合添加元素元素
print('给集合添加元素'.center(30, '*'))
list_1.add(999)
list_1.update([888,777,555])
print(list_1)

print('删除元素'.center(30, '*'))
# 随机移除元素
print(list_1.pop())
print(list_1.pop())
print(list_1)
# 删除集合中指定的元素
list_1.remove(999)
print(list_1)
# 删除集合中指定的元素
list_1.discard(888)
print(list_1)

print('浅拷贝，清理集合'.center(30, '*'))
list_5 = list_1.copy() # 浅拷贝
list_1.clear() # 移除集合中的所有元素
print(list_5)
print(list_1)

