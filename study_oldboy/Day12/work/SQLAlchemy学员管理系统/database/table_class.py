#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-23 10:34
# @Author  : liuyang
# @File    : table_class.py
# @Software: PyCharm

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, mapper
from sqlalchemy import func
from sqlalchemy import DATE, Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Table
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import setting

user = setting.DATABASE['user']
password = setting.DATABASE['password']
ip = setting.DATABASE['ip']
port = setting.DATABASE['port']
database = setting.DATABASE['database']

engine = create_engine(
    "mysql+pymysql://%s:%s@%s:%d/%s?charset=utf8" % (user, password, ip, port, database),
    # echo = True, # 输出日志
    max_overflow = 0,  # 超过连接池大小外最多创建的连接
    pool_size = 5,  # 连接池大小
    pool_timeout = 30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle = -1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

Base = declarative_base()  # 生成orm基类


teacher_m2m_classes = Table('teacher_m2m_classes', Base.metadata,
                        Column('teacher_id',Integer,ForeignKey('teacher.id')),
                        Column('classes_id',Integer,ForeignKey('classes.id')),
                        )

student_m2m_classes = Table('student_m2m_classes', Base.metadata,
                        Column('student_id',Integer,ForeignKey('student.id')),
                        Column('classes_id',Integer,ForeignKey('classes.id')),
                        )

# 学生上课记录表
study_record = Table('study_record', Base.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('course_record_id',Integer,ForeignKey('course_record.id')),
                    Column('student_id',Integer,ForeignKey('student.id')),
                    Column('status', String(8), nullable=True),
                    Column('score', Integer, nullable=True),
                    )
class StudyRecord(object):
    def __init__(self, id, course_record_id, student_id, status, score):
        self.id = id
        self.course_record_id = course_record_id
        self.student_id = student_id
        self.status = status
        self.score = score
mapper(StudyRecord, study_record)   # 表元数据与表构造分开创建，然后通过mapper（）函数与用户类关联

class Teacher(Base):
    """老师表"""
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    password = Column(String(64), nullable=False)

class Student(Base):
    """学生表"""
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    qq = Column(String(32), nullable=False, unique=True)

    course_record = relationship('CourseRecord', secondary=study_record, backref='student')

class Classes(Base):
    """课程表"""
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    classes_name = Column(String(32), nullable=False, unique=True)
    course = Column(String(64), nullable=False)

    teacher = relationship('Teacher', secondary=teacher_m2m_classes, backref='classes')
    student = relationship('Student', secondary=student_m2m_classes, backref='classes')

class CourseRecord(Base):
    """课程上课记录表"""
    __tablename__ = 'course_record'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    classes_id = Column(Integer, ForeignKey('classes.id'))

    classes = relationship("Classes", backref="course_record")

# class StudyRecord(Base):
#     """学生上课课程记录表"""
#     __tablename__ = 'study_record'
#     id = Column(Integer, primary_key=True)
#     status = Column(String(32), nullable=True)
#     course_record_id = Column(Integer, ForeignKey('course_record.id'), nullable=True)
#     student_id = Column(Integer, ForeignKey('student.id'), nullable=True)
#     score = Column(Integer, nullable=True)
#
#     course_record = relationship("CourseRecord", backref="study_record")
#     student = relationship("Student", backref="study_record")


session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = session_class()  # 生成session实例

def init_teacher_data():
    """系统中无管理老师的模块，所以这里初始化老师表数据"""
    t1 = Teacher(name='liuyang', password='123456')
    t2 = Teacher(name='zhangjuan', password='123456')
    t3 = Teacher(name='lyzj', password='123456')
    session.add_all([t1, t2, t3])
    session.commit()
    session.close()

if __name__ == '__main__':
    # 删除表
    Base.metadata.drop_all(engine)
    # 创建表
    Base.metadata.create_all(engine)  # 创建表结构
    init_teacher_data()