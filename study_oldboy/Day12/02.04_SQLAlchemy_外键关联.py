#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-17 9:31
# @Author  : liuyang
# @File    : 02.03_SQLAlchemy_外键关联.py
# @Software: PyCharm

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func
from sqlalchemy import DATE, Enum
from sqlalchemy import ForeignKey

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

class StudyRecord(Base):
    __tablename__ = 'study_record'  # 表名
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey('student.id'))

    student = relationship("Student", backref="my_study_record")  # 这个nb，允许你在user表里通过backref字段反向查出所有它在study_record表里的关联项

    def __repr__(self):
        return "<stu_id:%d day:%d status:%s>" % (self.stu_id, self.day, self.status)


# 创建表
# Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# 插入
# s1=Student(name='Alex', register_date="2019-01-09", gender='M')
# s2=Student(name='Jack', register_date="2019-01-09", gender='F')
#
# study_obj1=StudyRecord(day=1, status="Yes", stu_id=1)
# study_obj2=StudyRecord(day=2, status="NO", stu_id=1)
# study_obj3=StudyRecord(day=3, status="Yes", stu_id=1)
#
# Session.add_all([s1, s2, study_obj1, study_obj2, study_obj3])
# Session.commit()


# 查询
stu_obj = Session.query(Student).filter(Student.id == 1).first()
print(stu_obj)
print(stu_obj.my_study_record)

study_obj = Session.query(StudyRecord).filter(StudyRecord.id == 3).first()
print(study_obj)
print(study_obj.student)
