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
from sqlalchemy import Table

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

# 多对多外键，metadata方式创建Table
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)
    gender = Column(Enum("M", "F"), nullable=False)

class StudyRecord(Base):
    """外键关联Student"""
    __tablename__ = 'study_record'  # 表名
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey('student.id'))
    student = relationship("Student", backref="my_study_record")

session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = session_class()  # 生成session实例

def print_student(data):
    for item in data:
        print(item.id, item.name, item.register_date, item.gender)

def get_student(*args):
    """多条件查询"""
    return session.query(Student).filter(*args).all()

def put_student(name, register_date, gender):
    """数据插入"""
    student_obj = Student(name=name, register_date=register_date, gender=gender)
    session.add(student_obj)
    session.commit()

# print_student(get_student(Student.id<10, Student.id>2))
# print_student(session.query(Student).filter(Student.id<10, Student.id>2).all())

put_student('lytest', '2021-03-23', 'M')
print_student(get_student(Student.name == 'lytest'))
