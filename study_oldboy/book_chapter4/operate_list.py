#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang
my_family = []
my_family = ['me', 'wife', 'father', 'mom', 'daughter', 'son']
for member in my_family:
    print(member)

num = list(range(1,10,2))
print(num)

squares = []
for i in range(1,11):
    square = i ** 2
    squares.append(square)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares2 = [i**2 for i in range(1,11,2)]
print(squares2)

print(squares[0:3])
print(squares[:3])
print(squares[3:])

for i in squares[:3]:print(i)

squares1 = squares    # 指向一个列表
print(squares1)

del squares[-1]
print(squares)
print(squares1)

