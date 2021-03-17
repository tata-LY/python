#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-17 8:47
# @Author  : liuyang
# @File    : 02.01_SQLAlchemy_add.py
# @Software: PyCharm


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import DATE, Enum
import random

# engine = create_engine("mysql+pymysql://python:Python@123@192.168.113.11/pythondb",encoding='utf-8', echo=True)   # echo 打印日志
engine = create_engine("mysql+pymysql://python:Python@123@192.168.113.11/pythondb",encoding='utf-8')

Base = declarative_base()  # 生成orm基类

class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)
    gender = Column(Enum("M", "F"), nullable=False)

    def __repr__(self):
        return "<id:%s name:%s>" % (self.id, self.name)

# 创建表
# Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例


for i in range(1000):
    name = "name" + str(i).rjust(3,'0')
    date = '2021-03-17'
    gender = random.choice(['M', 'F'])
    obj = Student(name=name, register_date=date, gender=gender)
    Session.add(obj)

Session.commit()  # 现此才统一提交，创建数据

