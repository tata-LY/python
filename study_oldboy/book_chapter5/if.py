#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

print('a' == 'A')
print('a' == 'A'.lower())

family_list = ['dog', 'me', 'wife', 'father', 'mom', 'daughter', 'son']

if 'dog' in family_list:
    print("This is my dog.")
if 'wife' in family_list:
    print("my wife is zhangjuan.")
if 'father' in family_list:
    print("my father is liu.")

for member in family_list:
    if member == 'wife':
        print('she is zhangjuan.')

if family_list:
    print("ok")
else:
    print("no")