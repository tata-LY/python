#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

name = "my name is Liu\tYangYang. my wife is {name}, age is {age}."
name1 = "刘洋"
name2 = "liuyang"
name3 = "123"
name4 = "liuyang1"

print (name.capitalize())       # 只有第一个字母大写 My name is liu	yangyang. my wife is {name}, age is {age}.
print(name.count("L"))          # 1
print(name.center(50, '-'))     # my name is Liu	YangYang. my wife is {name}, age is {age}.

print(name1.encode())           # b'\xe5\x88\x98\xe6\xb4\x8b'
print(name1.encode().decode())  # 刘洋
print(name.endswith('Yang'))    # False
print(name.expandtabs(tabsize=10))  # my name is Liu      YangYang. my wife is {name}, age is {age}.

print(name.find('Y'))           # 15
print(name[0:8])                # my name

print(name.format(name='zhangjuan', age=26))        # my name is Liu	YangYang. my wife is zhangjuan, age is 26.
print(name.format_map({'name':'zhangjuan', 'age':26}))      # my name is Liu	YangYang. my wife is zhangjuan, age is 26.

print(name.isalnum())       # False
print(name2.isalnum())   # True 只包含数字或者字母

print(name2.isalnum())  # True
print(name3.isdigit())  # True


print('1a'.isidentifier())   # False # 是不是合法的变量

num = 1.1
#print(num.isdecimal())
print('33'.isnumeric())     # True

print(' '.isspace())        # True
print('Liuyang Yang'.istitle())         # True
print('Liuyang Yang'.isprintable())  # True # tty file  drive file 不能打印
print('LiuYang'.isupper())      # False

print('Liuyang'.join("--"))     # -Liuyang-
print("+".join(['1', '2', '3']))    # 1+2+3

print(name3.ljust(50, '-'))     # 123-----------------------------------------------

print('LiuYang'.lower())        # liuyang
print('LiuYang'.upper())        # LIUYANG

print('\nLiuYang\n'.lstrip())               # LiuYang\n
print('\nLiuYang\n'.rstrip())               # \nLiuYang
print('\nLiuYang\n'.strip())                # LiuYang

p = str.maketrans('abcdef', '123456')       # LiuYang
print("liuyang".translate(p))               # liuy1ng

print('liuyangyang'.replace('a', 'A'))      # liuyAngyAng
print('liuyangyang'.replace('a', 'A', 1))   # liuyAngyang

print('liuyangyang'.rfind('y'))             # 7

print('liu yang yang'.split())              # ['liu', 'yang', 'yang']
print('liu:yang:yang'.split(':'))           # ['liu', 'yang', 'yang']
print('liu\nyang\nyang'.splitlines())       # ['liu', 'yang', 'yang']

print('LiuYang'.swapcase())                 # lIUyANG
print("liu yang yang".title())              # Liu Yang Yang

print("liuyang".zfill(50))   # 0 补齐         # 0000000000000000000000000000000000000000000liuyang

