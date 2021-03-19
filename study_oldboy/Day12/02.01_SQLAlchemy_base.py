#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-16 15:09
# @Author  : liuyang
# @File    : 02.01_SQLAlchemy.py
# @Software: PyCharm

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func
from sqlalchemy import DATE, Enum
from sqlalchemy import ForeignKey


# engine = create_engine("mysql+pymysql://python:Python@123@192.168.113.11/pythondb",encoding='utf-8', echo=True)   # echo 打印日志
engine = create_engine("mysql+pymysql://python:Python@123@192.168.113.11/pythondb",encoding='utf-8')

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<id:%s name:%s>" % (self.id, self.name)

class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)
    gender = Column(Enum("M", "F"), nullable=False)

    def __repr__(self):
        return "<id:%s name:%s>" % (self.id, self.name)


# 删除表
# Base.metadata.drop_all(engine)

# 创建表
Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例


# 插入
user_obj = User(name="liuyang", password="123456")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
Session.commit()  # 现此才统一提交，创建数据


# 查询
# date = Session.query(User).filter_by(name='liuyang').first()
# data = Session.query(User).filter_by(name='liuyang').all()    # filter_by使用

# filter使用
# data = Session.query(User).filter(User.name=='liuyang').all() # 全部
# data = Session.query(User).filter(User.id>3).filter(User.id<8).all()    # 多条件
data = Session.query(User).filter(User.id==1).first()
print(data)

# # 修改
# data.name = 'Liu Yang'
# data.password = '654321'
# Session.commit()


# 回滚
fake_user = User(name='Rain', password='12345')
Session.add(fake_user)
print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据
Session.rollback()  # 此时你rollback一下
print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。

# 统计
print(Session.query(User).filter(User.id>3).filter(User.id<8).count())

# 分组 group by
print(Session.query(func.count(User.name), User.name).group_by(User.name).all())

# 删除数据
Session.query(User).filter(User.id > 10).delete()
Session.commit()

# 连表查询
print(Session.query(User, Student).filter(User.id==Student.id).all())

Session.close()