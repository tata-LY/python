#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import payment

# payment.credit_card_pay('ly', '123456', 100000)
# payment.bank_card_pay('ly', '123456', 100000)

pay_method = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
money = int(sys.argv[4])

if pay_method == 'credit':
    if payment.credit_card_pay(username, password, money):
        print('credit支付成功！')
    else:
        print('credit支付失败！')
elif pay_method == 'bank':
    if payment.bank_card_pay(username, password, money):
        print('bank支付成功！')
    else:
        print('bank支付失败！')