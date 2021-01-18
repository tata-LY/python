#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-15 10:54
# @Author  : liuyang
# @File    : 1.py
# @Software: PyCharm


def get_user_info(database, name):
    data = {}
    f_r = open(database, 'r', encoding='utf-8')
    for line in f_r.readlines():
        if name == line.strip().split(":")[0]:
            data['name'], data['passwd'], data['clok'] = line.strip().split(":")
    f_r.close()
    return data

def update_user_clok(database, name):
    data = ''
    f_r = open(database, 'r', encoding='utf-8')
    for line in f_r.readlines():
        if name == line.strip().split(":")[0]:
            data += ':'.join((name, line.strip().split(":")[0], '1\n'))
        else:
            data += line
    f_r.close()
    f_w = open(database, 'w', encoding='utf-8')
    f_w.write(data)
    f_w.close()

def main():
    database = './user_info'
    print('用户登陆'.center(20, '-'))
    user = input("用户名：")
    passwd = input("密码：")
    user_data = get_user_info(database, user)
    count = 1
    if user_data:
        if user_data['clok'] == '0':
            while True:
                if passwd == user_data['passwd']:
                    exit("%s 欢迎登陆！" % user)
                else:
                    if count < 3:
                        passwd = input("密码错误%d次,请重新输入密码：" % count)
                        count += 1
                    else:
                        update_user_clok(database, user)
                        exit('密码连续错误3次，用户锁住！')
        else:
            exit('用户已被锁住，等待解锁后重试！')
    else:
        exit('用户未注册！')




if __name__ == '__main__':
    main()