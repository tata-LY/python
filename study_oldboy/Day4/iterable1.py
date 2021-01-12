#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from collections import Iterable, Iterator

print(isinstance('abc', Iterable))
print(isinstance((x*x for x in range(10)), Iterator))

a = [x*x for x in range(10)]
print(a)
a = iter(a)
print(a)

a.__next__()
a.__next__()