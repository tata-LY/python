#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

print("集合关系性测试".center(30, "-"))
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = [2, 4, 6, 8, 10]
b = [1, 3, 5, 7, 9]
c = set([1, 2, 5, 8, 9])

a = set(a)
b = set(b)

print(a,type(a),b,type(b))

# 取并集
print("并集")
print(a.union(b))
print(a | b)
d = a.union(b)
print(a, b, c)

print("交集")
print(c.intersection(b))    # 取交集
print(c & b)

print("差集")
print(c.difference(b))   # 取差集 in c but not in b
print(c - b)

print("子集父集")
print(a.issubset(d))     # 判断a是不是d的子集
print(d.issuperset(a))   # 判断d是不是a的父集

print("对称差集")
print(c.symmetric_difference(b))  # 对称差集  not in c  and not in b
print(c ^ b)

print(a.isdisjoint(b)) # 判断没有交集
print(a.isdisjoint(c))

set_1 = set([])
set_1.add(1)  # 单个添加
set_1.update([1,2,3,4,5,6,7,8,9,10])  # 添加多个
print(set_1)

set_1.remove(1)
item = set_1.pop()
set_1.discard(3)
set_1.discard(11)  # 不存在不会报错

print(set_1, item)


print(len(set_1))

print(2 in set_1)   # list dict set 都可以这样判断
print(2 not in set_1)


