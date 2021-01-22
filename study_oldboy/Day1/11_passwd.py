#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

import getpass

_username = "liuyang"
_password = "123456"

username = input("username:")
password= getpass.getpass("password:")

if username == _username and password == _password:
	print("Welcom user {name} login...".format(name=username))
else:
	print("Invalib username or password!")

# print(username,password)