#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

from conf import settings
import os
import sys
import json

def file_db_select(id, password):
    database_type = settings.DATABASE
    account_file = "%s/%s.json" %(database_type['path'], id)
    if os.path.exists(account_file):
        with open(account_file, "r", encoding="utf-8") as f_r:
            account_data = json.loads(f_r.read())
            if account_data['password'] == password:
                return account_data

def mysql_db_select(id, password):
    pass

def db_select(id, password):
    database_type = settings.DATABASE
    if database_type['engine'] == 'file_storage':
        return file_db_select(id, password)
    if database_type['engine'] == 'mysql':
        return mysql_db_select(id, password)


def file_db_add(user_data):
    database_type = settings.DATABASE
    account_file = "%s/%s.json" %(database_type['path'], user_data['id'])
    if os.path.exists(account_file):
        return False
    else:
        with open(account_file, "w", encoding="utf-8") as f_w:
            f_w.write(json.dumps(user_data))
        return True

def mysql_db_add(user_data):
    pass

def db_add(user_data):
    database_type = settings.DATABASE
    if database_type['engine'] == 'file_storage':
        return file_db_add(user_data)
    if database_type['engine'] == 'mysql':
        return mysql_db_add(user_data)


def file_db_update(user_data):
    database_type = settings.DATABASE
    account_file = "%s/%s.json" %(database_type['path'], user_data['id'])
    with open(account_file, "w", encoding="utf-8") as f_w:
        f_w.write(json.dumps(user_data))
    return True

def mysql_db_update(user_data):
    pass

def db_update(user_data):
    database_type = settings.DATABASE
    if database_type['engine'] == 'file_storage':
        return file_db_update(user_data)
    if database_type['engine'] == 'mysql':
        return mysql_db_update(user_data)