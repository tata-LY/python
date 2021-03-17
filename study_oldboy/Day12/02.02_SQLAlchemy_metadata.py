#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-16 15:19
# @Author  : liuyang
# @File    : 02.02_SQLAlchemy_metadata.py
# @Software: PyCharm

from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table('user2', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password


mapper(User, user)  # the table metadata is created separately with the Table construct, then associated with the User class via the mapper() function