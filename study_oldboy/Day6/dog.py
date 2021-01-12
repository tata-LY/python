#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

class Dog:
    def __init__(self, name):
        self.name = name
    def bulk(self):
        print("{dog_name}: wang wang wang ...".format(dog_name=self.name))


d1 = Dog("Dog1")
d2 = Dog("Dog2")
d3 = Dog("Dog3")

d1.bulk()
d2.bulk()
d3.bulk()