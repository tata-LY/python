#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

def hello(username="World"):
    print("Hello, {username} !".format(username=username))

hello()
hello(username="Liuyang")

def SUM(num=100):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum

sum = SUM(num=10)
print(sum)

def hello(names=[]):
    for name in names:
        print("Hello, {name} !".format(name=name))
names = ["LiuYang", "ZhangJuan"]
hello(names=names)


def before_after(before_list=[], after_list=[]):
    while before_list:
        current = before_list.pop()
        after_list.append(current)

before_list = [1, 2, 3]
after_list = []
before_after(before_list=before_list, after_list=after_list)
print(before_list, after_list)

before_list2 = [1, 2, 3]
after_list2 = []
before_after(before_list2[:], after_list=after_list2)   # 这样传参list就不会被修改了
print(before_list2, after_list2)

def names(*names):
    print(names,type(names))
names(1)
names(1, "a")
