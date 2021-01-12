#!/usr/bin/env python3
# _*_coding:utf-8_*_
# by liuyang

# 用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

import hashlib

# md5
m = hashlib.md5()
m.update(b"hello")
print(m.digest())
print(m.hexdigest())

m.update(b"It's me")
print(m.digest())
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b"helloIt's me")  # 等于上面两次update拼接
print(m2.digest())
print(m2.hexdigest())

# sha1
s1 = hashlib.sha1()
s1.update(b"helloIt's me")
print(s1.hexdigest())

# 其他类似

import hmac
h = hmac.new(b'liu', b"yang")
h.update(b'hellowo')
print(h.digest())
print(h.hexdigest())  # 十六进制

h2 = hmac.new("刘洋".encode(encoding="utf-9"))
print(h2.hexdigest())