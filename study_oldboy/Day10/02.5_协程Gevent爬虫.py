#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-3 9:36
# @Author  : liuyang
# @File    : 02.5_协程Gevent爬虫.py
# @Software: PyCharm

from urllib.request import urlopen
import gevent
import time
from gevent import monkey

monkey.patch_all()      # 把当前程序的所有的IO操作给我单独的做上标记


def f(url):
    print("GET: %s" % url)
    resp = urlopen(url)
    data = resp.read()
    print("%s bytes received from %s." % (len(data), url))
    # print(data)

urls = [
    "https://www.python.org/",
    "https://www.baidu.com/",
    "https://weibo.com/"
]

# 串行执行
start_time = time.time()
for url in urls:
    f(url)
end_time = time.time()
print("串行执行所花时间：%s" % (end_time - start_time))      # 串行执行所花时间：0.7645776271820068

async_start_time = time.time()
gevent.joinall(
    [
        gevent.spawn(f, "https://www.python.org/"),
        gevent.spawn(f, "https://www.baidu.com/"),
        gevent.spawn(f, "https://weibo.com/")
    ]
)
async_end_time = time.time()
print("geven异步执行所花时间：%s" % (async_end_time - async_start_time))     # geven异步执行所花时间：0.37825512886047363