#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-29 9:06
# @Author  : liuyang
# @File    : 3.1_inherit继承.py
# @Software: PyCharm

# class People:     # 经典类
class People(object):   # 新式类，继承上有不同
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def __print(self, data):
        """私有方法不能被继承"""
        print("\033[31;1m{data}\033[0m".format(data=data))

    def eat(self):
        self.__print("%s is eating ..." % self.name)

    def sleep(self):
        self.__print(("%s is sleeping ..." % self.name))

    def sleep2(self):
        self.__print(("%s is sleeping ..." % self.name))

    def show_info(self):
        self.__print("name: {name}, age: {age}".format(name=self.name, age=self.age))

class Relation(object):
    def make_friends(self, obj):    # obj对象
        print("%s is making friends with %s" % (self.name, obj.name))
        self.friends.append(obj)    # 通过obj对象一直保持联系

class Man(People, Relation):  # 继承了class People和Relation
    def __init__(self, name, age, money):
        """重构父类的构造函数"""
        # People.__init__(self, name, age)
        super(Man, self).__init__(name, age)    # 新式类写法，与上面写法效果一样
        self.money = money
        print("%s一出生就有%s块钱" % (self.name, self.money))

    def piao(self):
        # self.__print("%s is piaoing .... 30s .... done" % self.name)  # 私有方法不能被继承 AttributeError: 'Man' object has no attribute '_Man__print'
        print("%s is piaoing .... 30s .... done" % self.name)

    def sleep(self):
        """完全覆盖了父类的sleep方法"""
        print("man is sleeping")

    def sleep2(self):
        """重构父类的方法"""
        # People.sleep2(self)
        super(Man, self).sleep2() # 新式写法，与上面People.sleep2(self)一样
        print("重构父类sleep2方法")

class   Woman(People, Relation):
    def get_birth(self):
        print("%s is borning a baby ... " % self.name)

m1 = Man('Alex', 20, 10000)     # Alex一出生就有10000块钱
m1.eat()        # Alex is eating ...
m1.piao()       # Alex is piaoing .... 30s .... done
m1.sleep()      # man is sleeping
m1.sleep2()     # Alex is sleeping ...\n重构父类sleep2方法

w1 = Woman('Chengronghua', 20)
w1.get_birth()      # Chengronghua is borning a baby ...

w2 = Woman('Mrs Wang', 38)

m1.make_friends(w1)     # Alex is making friends with Chengronghua
m1.make_friends(w2)     # Alex is making friends with Mrs Wang
print(m1.friends)       # [<__main__.Woman object at 0x00000274A487DF40>, <__main__.Woman object at 0x00000274A49F8CD0>]
print(m1.friends[0].name)       # Chengronghua
print(m1.friends[1].name)       # Mrs Wang

w2.name = '王女士'     # 如果w2改名了,通过obj还是可以关联
print(m1.friends[1].name)       # 王女士
