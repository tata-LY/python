#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-17 10:46
# @Author  : liuyang
# @File    : 02.05_SQLALchemy_api.py
# @Software: PyCharm

import orm_many_fk
from sqlalchemy.orm import sessionmaker

session_class = sessionmaker(bind=orm_many_fk.engine)
session = session_class()

# 数据插入
# address1 = orm_many_fk.Address(street="Nanshan", city="ShenZhen", state="GD")
# address2 = orm_many_fk.Address(street="Futian", city="ShenZhen", state="GD")
# address3 = orm_many_fk.Address(street="Longhua", city="ShenZhen", state="GD")
# session.add_all([address1, address2, address3])
#
# customer1 = orm_many_fk.Customer(name="Liuyang", billing_address=address1, shipping_address=address2)
# customer2 = orm_many_fk.Customer(name="Zhangjuan", billing_address=address3, shipping_address=address2)
# session.add_all([customer1, customer2])

# session.commit()

customer_obj = session.query(orm_many_fk.Customer).filter(orm_many_fk.Customer.name == "Liuyang").first()
print(customer_obj.name, customer_obj.billing_address, customer_obj.shipping_address)

session.close()