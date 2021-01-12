#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

def login_required(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        res = func(*args, **kwargs)
        return res
        # if is_auth:
        #     func(*args, **kwargs)
        # else:
        #     exit("User is not authenticated.")
    return wrapper

@login_required
def test1(name):
    print(name)
    print(name)
    return 'ok'

print(test1('liuyang'))