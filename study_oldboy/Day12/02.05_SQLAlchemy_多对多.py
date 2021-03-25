#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-17 13:32
# @Author  : liuyang
# @File    : 02.05_SQLAlchemy_多对多.py
# @Software: PyCharm

from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# engine = create_engine("mysql+pymysql://python:Python@123@192.168.113.11/pythondb",encoding='utf-8')
# 支持中文
engine = create_engine("mysql+pymysql://python:Python@123@192.168.113.11/pythondb?charset=utf8")

Base = declarative_base()

# metadata方式创建Table
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

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# 创建表
# Base.metadata.create_all(engine)  # 创建表结构

# 数据插入
# b1 = Book(name="book1")
# b2 = Book(name="book2")
# b3 = Book(name="book3")
# b4 = Book(name="book4")
#
# a1 = Author(name="liuyang")
# a2 = Author(name="zhuangjuan")
# a3 = Author(name="alex")

#
# b1.authors = [a1, a2]
# b2.authors = [a1, a2, a3]
# b3.authors = [a1]
# b4.authors = [a2]


# session.add_all([b1, b2, b3, b4, a1, a2, a3])
# session.commit()

# b5 = Book(name="book5")
# b6 = Book(name="book6")
# a4 = Author(name="name4")
# a5 = Author(name="name5")
# a4.books = [b5, b6]
# a5.books = [b5]
# session.add_all([b5, b6, a4, a5])
# session.commit()

# 添加books，与已有的authors数据关联
# b7 =Book(name="book7")
# a1 = session.query(Author).filter(Author.name == "name4").first()
# a2 = session.query(Author).filter(Author.name == "name5").first()
# b7.books = [a1, a2]
# session.add_all([b7])
# session.commit()



# 中文数据插入
# b1 = Book(name="书籍1")
# b2 = Book(name="书籍2")
# b3 = Book(name="书籍3")
#
# a1 = Author(name="刘洋")
# a2 = Author(name="张娟")
#
# b1.authors = [a1, a2]
# b2.authors = [a1]
# b3.authors = [a2]
#
# session.add_all([b1, b2, b3, a1, a2])
# session.commit()


# 数据查询
# 通过author查book
# author_obj = session.query(Author).filter(Author.name == "liuyang").first()
# print(author_obj)           # liuyang
# print(author_obj.books)     # [book1, book2, book3]
# # 通过book查author
# book_obj = session.query(Book).filter(Book.id == 5).first()
# print(book_obj)             # 书籍1
# print(book_obj.authors)     # [张娟, 刘洋]

"""
多对多删除
删除数据时不用管boo_m2m_authors　， sqlalchemy会自动帮你把对应的数据删除
"""
# 通过书删除作者
# del_author_obj = session.query(Author).filter(Author.name == 'Alex').first()
# del_book_obj = session.query(Book).filter(Book.name == 'book2').first()
#
# del_book_obj.authors.remove(del_author_obj) # 从一本书里删除一个作者
# session.commit()
