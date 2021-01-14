#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

my_family = {'wife': 'zhangjuan', 'father': 'liudongke', 'mother': 'shushuyuan', 'myself': 'liuyang'}
my_family = {
    'wife': 'zhangjuan',
    'father': 'liudongke',
    'mother': 'shushuyuan',
    'myself': 'liuyang'
}
print(my_family)
print(my_family['myself'])

my_family['son'] = 'liuyiyi'
print(my_family)

alien = {'x': 0, 'y': 0, 'speed': 'slow'}
if alien['speed'] == 'slow':
    alien['x'] = alien['x'] + 1
elif alien['speed'] == 'media':
    alien['x'] = alien['x'] + 2
else:
    alien['x'] = alien['x'] + 3

print(alien)

del my_family['son']
print(my_family)


for key,value in my_family.items():
    print("my {member} : {name}".format(member=key, name=value))

print(my_family.items())

print(my_family.keys())
for key in  my_family.keys():
    print(key)

if 'son' not in my_family.keys():
    print("yes")
else:
    print("no")

for key in sorted(my_family.keys()):
    print(key)

for value in sorted(my_family.values()):
    print(value)

my_family['mom'] = 'shushuyuan'
print(my_family)

for value in sorted(set(my_family.values())):    # 排序 去重
    print(value)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
alien = [alien_0, alien_1, alien_2]
print(alien)

my_family1 = {'wife': ['zhangjuan', 26], 'father': ['liudongke', 50], 'mother': ['shushuyuan', 48], 'myself': ['liuyang', 27]}
print(my_family1['wife'])

for key,value in my_family1.items():
    if key != 'myself':
        print("my {member} name is {name}, age is {age}".format(member=key, name=value[0], age=value[1]))

alien = []

for i in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien.append(new_alien)

print(alien)

for i in alien[:3]:
    i['color'] = 'yellow'
    i['points'] = 10
    i['speed'] = 'media'

print(alien)


my_family2 = {
    'wife': {
        'name': 'zhangjuan',
        'age': 26
    },
    'father': {
        'name': 'liudongke',
        'age': 50
    },
    'mother': {
        'name': 'shushuyuan',
        'age': 48
    }
}

print(my_family2)
for key,value in my_family2.items():
    print("my {member} name is {name}, age is {age}".format(member=key, name=value['name'], age=value['age']))



