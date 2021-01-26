#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-1-18 10:57
# @Author  : liuyang
# @File    : consumer.py
# @Software: PyCharm

import os
import sys
from core import common
from conf import settings

def shopping():
    goods_file = settings.goods_file
    goods_data = {}
    goods_cart = []
    result = common.read_file(goods_file) # list
    if result:
        count = 1
        for _, val in enumerate(result):
            goods_data[str(count)] = val.rstrip()  # rstrip()删除右侧换行符
            count += 1
    else:
        common.print_error('无商品存在！')
    print('购物中'.center(30, '*'))
    while True:
        your_choice = common.choice(goods_data)
        goods_cart.append(goods_data[your_choice])
        is_continue = input('是否继续添加商品到购物车[Y/y]>>>')
        if is_continue not in ['Y', 'y', 'yes']:
            break

    print('购物车：%s' % goods_cart)
    is_pay_credit = input('是否信用卡支付[Y/y]').strip()
    if is_pay_credit in ['Y', 'y', 'yes', 'YES']:
        pay_method = 'credit'
    else:
        pay_method = 'bank'
    print('银行卡登录'.center(50, '-'))
    username = input('用户名>>>').strip()
    password = input('密码>>>').strip()
    total = 0
    for _, val in enumerate(goods_cart):
        total += int(val.split(':')[1].lstrip())        # 购物总金额
    # 调用ATM接口,这里通过直接执行ATM的python文件来调用。
    atm_pay_file = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/Atm' + '/bin/atm_pay.py'
    os.system('python {atm_pay_file} {pay_method} {username} {password} {total}'.format(atm_pay_file=atm_pay_file, pay_method=pay_method, username=username, password=password, total=total))
    input('输入回车键继续>>>')


def main():
    option = {
        '1': '购买商品',
        'b': '返回',
        'q': '退出系统'
    }
    while True:
        choice = common.choice(option)
        if choice == '1':
            shopping()
        elif choice == 'b':
            break
        elif choice == 'q':
            exit("欢迎下次光临！")



