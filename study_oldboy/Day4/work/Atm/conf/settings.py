#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGS_LEVEL = "INFO"

LOGS_TYPES = {
    'access': 'access.log',
    'atm': 'atm.log'
}

DATABASE = {
    'engine': 'file_storage',  # mysql
    'name': 'account',
    'path': '%s/db/' % BASE_DIR,
    'ip' : None,
    'port': None,
    'user': None,
    'password':None,
}

TRANSACTION_TYPE = {
    'save_money': {'action': 'plus', 'interest': 0},
    'repay': {'action': 'minus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.002},
    'transfer': {'action': 'minus', 'interest': 0},
}