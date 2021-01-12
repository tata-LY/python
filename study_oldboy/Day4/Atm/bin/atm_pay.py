#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import payment

payment.credit_card_pay('ly', '123456', 100000)
payment.bank_card_pay('ly', '123456', 100000)