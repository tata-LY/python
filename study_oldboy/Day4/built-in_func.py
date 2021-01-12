#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

print(all([0, 1, 2]))
print(all([1, 2, 3]))

print(any([0, 1]))
print(ascii([1, 2, "中文"]))

print(bin(5))

# bytearray 可以修改字符串
b = bytearray("abcde", encoding="utf-8")
print(b)
b[0] = 108
print(b)

print(callable([]))

print(chr(97))
print(ord('a'))

print(dir(b))

res1 = lambda x,y: x*y
print(res1(1,2))

#if 条件为真的时候返回if前面内容，否则返回0
exp1= lambda x:x+1 if  x==1 else 0
print(exp1(1))

res2 = filter(lambda n:n>5,range(10))
for i in res2:
    print(i)

res3 = map(lambda n:n*2, range(10))
for i in res3:
    print(i)
res4 = [lambda n:n*n, range(1,10)]
print(res4)

print(globals())


print(hex(26))

print(locals())

a = ["A", "B", "C", "D"]
b = ["a", "b", "c"]
for i in zip(a, b):
    print(i)