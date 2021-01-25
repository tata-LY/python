#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

user, passwd = "liuyang", "123456"

def auth(auth_type):
    def out_warpper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                username = input("Username: ")
                password = input("Password: ")

                if username == user and password == passwd:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    result = func(*args, **kwargs)
                    print(result)
                    return result # 保持被装饰的函数的return
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ladp":
                print("no ladp")

        return wrapper() # 应该改成return wrapper
    return out_warpper

@auth(auth_type="local")
def home():
    print("Welcome to home page.")
    return "from home"

@auth(auth_type="ladp")
def bbs():
    print("Welcome to bbs page.")
    return "from bbs"