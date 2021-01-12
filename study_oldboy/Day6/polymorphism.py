#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

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
        print("Cat[%s]: Meow" % self.name)

class Dog(Animal):
    def talk(self):
        print("Dog[%s]: WangWang..." % self.name)



c = Cat("喵喵")
d = Dog("旺财")


Animal.animal_talk(c)
Animal.animal_talk(d)
