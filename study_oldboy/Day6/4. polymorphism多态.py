#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-29 11:21
# @Author  : liuyang
# @File    : 4. polymorphism多态.py
# @Software: PyCharm

class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print("Cat[%s]: Meow Meow ..." % self.name)

class Dog(Animal):
    def talk(self):
        print("Dog[%s]: Woof Woof ..." % self.name)

c = Cat("喵喵")
d = Dog("旺财")

Animal.animal_talk(c)
Animal.animal_talk(d)
