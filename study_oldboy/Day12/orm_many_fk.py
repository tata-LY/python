#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-17 10:36
# @Author  : liuyang
# @File    : 02.05_SQLAlchemy_多外键关联.py
# @Software: PyCharm

from sqlalchemy import Integer, ForeignKey, String, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://python:Python@123@192.168.113.11/pythondb",encoding='utf-8')

Base = declarative_base()

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return "%s %s %s" % (self.state, self.city, self.street)

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])

    # billing_address = relationship("Address")
    # shipping_address = relationship("Address")
"""
创建表结构是没有问题的，但你Address表中插入数据时会报下面的错
sqlalchemy.exc.AmbiguousForeignKeysError: Could not determine join
condition between parent/child tables on relationship
Customer.billing_address - there are multiple foreign key
paths linking the tables.  Specify the 'foreign_keys' argument,
providing a list of those columns which should be
counted as containing a foreign key reference to the parent table.
多个外键关联解决办法如下：
    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])
"""



# 创建表
# Base.metadata.create_all(engine)  # 创建表结构


