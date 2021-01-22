#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

name = input("name:")
age = int(input("age:"))
print(type(age),type(str(age)))
job = input("job:")

# raw_input puthon2.X
info1 = "------info1 of -------\n" + "Name:" + name + "\nAge:" + str(age)

info2 = '''
----------- info2 of %s -----------
Name:%s
Age:%d
Job:%s
''' %(name,name,age,job)

info3 = '''
----------- info3 of {_name} -----------
Name:{_name}
Age:{_age}
Job:{_job}
''' .format(_name=name,_age=age,_job=job)

print(info1,info2,info3)