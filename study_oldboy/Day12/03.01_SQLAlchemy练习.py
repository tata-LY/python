#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-18 16:34
# @Author  : liuyang
# @File    : 03.01_SQLAlchemy练习.py
# @Software: PyCharm

"""
单表增删改查
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func
from sqlalchemy import DATE, Enum
from sqlalchemy import ForeignKey

MYSQL_IP = '192.168.113.11'
MYSQL_PORT = 3306
MYSQL_USER = 'python'
MYSQL_PASSWORD = 'Python@123'
DATABASE = 'pythondb'

engine = create_engine(
    "mysql+pymysql://python:Python@123@192.168.113.11:3306/pythondb?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

Base = declarative_base()  # 生成orm基类

class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)
    gender = Column(Enum("M", "F"), nullable=False)

session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = session_class()  # 生成session实例

def get_student(id=None, name=None, register_date=None, gender=None):
    q = session.query(Student)
    if id:
        q = q.filter(Student.id == id)
    if name:
        q = q.filter(Student.name == name)
    if register_date:
        q = q.filter(Student.register_date == register_date)
    if gender:
        q = q.filter(Student.gender == gender)

    return q.all()

data = get_student(id=100)
print(data)
