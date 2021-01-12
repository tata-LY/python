#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

name = "my name is Liu\tYangYang. my wife is {name}, age is {age}."
name1 = "刘洋"
name2 = "liuyang"
name3 = "123"
name4 = "liuyang1"

print (name.capitalize())   # 只有第一个字母大写
print(name.count("L"))
print(name.center(50, '-'))

print(name1.encode())
print(name1.encode().decode())
print(name.endswith('Yang'))
print(name.expandtabs(tabsize=10))

print(name.find('Y'))
print(name[0:8])

print(name.format(name='zhangjuan', age=26))
print(name.format_map({'name':'zhangjuan', 'age':26}))

print(name.isalnum())
print(name2.isalnum())   # 只包含数字或者字母

print(name2.isalnum())
print(name3.isdigit())


print('1a'.isidentifier())   # 是不是合法的变量

num = 1.1
#print(num.isdecimal())
print('33'.isnumeric())

print(' '.isspace())
print('Liuyang Yang'.istitle())
print('Liuyang Yang'.isprintable())  # tty file  drive file 不能打印
print('LiuYang'.isupper())

print('Liuyang'.join("--"))
print("+".join(['1', '2', '3']))

print(name3.ljust(50, '-'))

print('LiuYang'.lower())
print('LiuYang'.upper())

print('\nLiuYang\n'.lstrip())
print('\nLiuYang\n'.rstrip())
print('\nLiuYang\n'.strip())

p = str.maketrans('abcdef', '123456')
print("liuyang".translate(p))

print('liuyangyang'.replace('a', 'A'))
print('liuyangyang'.replace('a', 'A', 1))

print('liuyangyang'.rfind('y'))

print('liu yang yang'.split())
print('liu:yang:yang'.split(':'))
print('liu\nyang\nyang'.splitlines())

print('LiuYang'.swapcase())
print("liu yang yang".title())

print("liuyang".zfill(50))   # 0 补齐

