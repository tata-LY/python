#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

family_list = []
family_list = ['me', 'wife', 'father', 'mother']
print(family_list)
print(family_list[2])
print(family_list[1].title())
print(family_list[-1])

family_list[3] = 'mom'
print(family_list)
family_list.append('son')
print(family_list)

family_list.insert(-1, 'daughter')   # 前插
family_list.insert(0, 'dog')
print(family_list)

del family_list[0]
print(family_list)

pop_member = family_list.pop(-1) # 默认删除最后一个
print(pop_member, family_list)

family_list.remove('daughter')
print(family_list)

family_list.sort()    # 永久排序
print(family_list)
family_list.sort(reverse=True)
print(family_list)

family_list = ['dog', 'me', 'wife', 'father', 'mom', 'daughter', 'son']
num_list = [34, 35, 3, 46, 1, 6, 3]
print(sorted(family_list), sorted(num_list))   # 临时排序
print(family_list, num_list)
num_list.sort(reverse=True)
print(num_list)

family_list.reverse()
print(family_list)

print(len(family_list))