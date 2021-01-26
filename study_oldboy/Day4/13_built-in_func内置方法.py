#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-26 8:33
# @Author  : liuyang
# @File    : 13_built-in_func内置方法.py
# @Software: PyCharm

"""
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
元素除了是 0、空、None、False 外都算 True
"""
print('all()'.center(70, '-'))
print(all([0, 1, 2]))   # False 0为False
print(all([1, 2, 3]))   # True

"""
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
元素除了是 0、空、FALSE 外都算 TRUE。
"""
print('any()'.center(70, '-'))
print(any([0, 1]))  # True


print(ascii([1, 2, "中文"]))  # [1, 2, '\u4e2d\u6587']

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
print('bin()'.center(70, '-'))
print(bin(5))   # 0b101

# bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
print('bytearray()'.center(70, '-'))
b = bytearray("abcde", encoding="utf-8")
print(b)    # bytearray(b'abcde')
b[0] = 108
print(b)    # bytearray(b'lbcde')

# callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。
print('callable、chr、ord、exec、dir、divmod'.center(70, '-'))
print(callable([])) # False
print(chr(97))      # a
print(ord('a'))     # 97

code = "print('hello world')"
exec(code)      # hello world

# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
print(dir(b))

# divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
print(divmod(5, 3))     # (1, 2)

print('lambda filter'.center(70, '-'))
res1 = lambda x,y: x*y
print(res1(1,2))    # 2

#if 条件为真的时候返回if前面内容，否则返回0
exp1= lambda x:x+1 if  x==1 else 0
print(exp1(1))      # 2

"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
"""
res2 = filter(lambda n:n>5,range(10))
for i in res2:
    print(i, end=' ')   # 6 7 8 9
print('')

res3 = map(lambda n:n*2, range(10))
for i in res3:
    print(i, end=' ')   # 0 2 4 6 8 10 12 14 16 18
print('')
res4 = [lambda n:n*n, range(1,10)]
print(res4)     # [<function <lambda> at 0x000001A2DF6CDC10>, range(1, 10)]

print('globals hex hash locals'.center(70, '-'))
# globals() 函数会以字典类型返回当前位置的全部全局变量。
print(globals())
print(globals()['__file__'])    # E:/刘洋工作/20200921/git/tata-LY/python/study_oldboy/Day4/13_built-in_func内置方法.py

# hash() 用于获取取一个对象（字符串或者数值等）的哈希值。
print(hash('liuyang'))  # 867805895196598148

# hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
print(hex(26))
# locals() 函数会以字典类型返回当前位置的全部局部变量。
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
print(locals())

"""
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
"""
print('map()'.center(70, '-'))
s1 = [1, 2, 3, 4]
def f1(s):
    if s != 1:
        return s**2
res1 = map(f1, s1)
print(res1, type(res1), list(res1)) # <map object at 0x000001C5E6E99FD0> <class 'map'> [None, 4, 9, 16] 不满足的用None补充,赋值为函数的return
print(res1, type(res1), list(res1)) # <map object at 0x00000271FDB6E9D0> <class 'map'> []
res2 = map(lambda x:x**2,range(10))
print(list(res2))   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print('oct reversed sorted'.center(70, '-'))
# 八进制
print(oct(8))   # 0o10
for i in reversed([1, 3, 2]):  # <list_reverseiterator object at 0x0000021BC28208B0>
    print(i, end=' ')   # 2 3 1
print('')
print(sorted([1, 3, 2]))    # [1, 2, 3]

"""
reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
"""
print('reduce()'.center(70, '-'))
from functools import reduce
def f2(x, y):
    return x + y
res1 = reduce(f2, range(1, 101))
res2 = reduce(lambda x,y:x+y,range(1,101))
print(res1, res2)      # 5050 5050

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
print('zip()'.center(70, '-'))
a = ["A", "B", "C", "D"]
b = ["a", "b", "c"]
for i in zip(a, b):     # <zip object at 0x0000022A6E0A75C0>
    print(i, end=' ')   # ('A', 'a') ('B', 'b') ('C', 'c')
