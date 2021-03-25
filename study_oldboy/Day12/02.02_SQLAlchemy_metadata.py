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
    def __init__(self, id, name, fullname, password):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.password = password


mapper(User, user)  # 表元数据与表构造分开创建，然后通过mapper（）函数与用户类关联