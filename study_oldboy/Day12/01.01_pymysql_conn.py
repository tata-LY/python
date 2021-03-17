#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-16 13:31
# @Author  : liuyang
# @File    : 01.01_mysql_conn.py
# @Software: PyCharm

import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.113.11', port=3306, user='python', passwd='Python@123', db='pythondb')

# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回受影响行数
effect_row = cursor.execute("select * from student")
print(effect_row)       # 行数
# print(cursor.fetchone())    # 一条条取数据
print(cursor.fetchmany(4))    # 获取前n行数据
print(cursor.fetchall())      # 取所有的

# 批量执行
data = [
    ("name1", "2021-03-16", 'M'),
    ("name2", "2021-03-16", 'F'),
    ("name3", "2021-03-16", 'F'),
    ("name4", "2021-03-16", 'M'),
]
cursor.executemany("insert into student (name, register_date, gender) values(%s, %s, %s)", data)

# 提交，不然无法保存新建或者修改的数据
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

