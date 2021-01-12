#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGS_LEVEL = "INFO"
LOGS_TYPES = {
    'access': 'access.log',
    'atm': 'atm.log',
    'course': 'course.log',
}

USER_TYPES = {
    '1': 'student',
    '2': 'teacher',
    '3': 'school',
}

DATABASE = {
    'engine': 'file_storage',  # mysql
    'name': 'account',
    'path': '%s/db' % BASE_DIR,
    'ip' : None,
    'port': None,
    'user': None,
    'password':None,
}

DATA_TABLE = {
    'teacher': 'teacher',
    'student': 'student',
    'course': 'course',
    'class': 'class'
}