#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-5 16:16
# @Author  : liuyang
# @File    : 03.7_Socket_Client.py
# @Software: PyCharm

import socket
import os

class FtpCient(object):
    def __init__(self, IP, PORT):
        self.client = socket.socket()
        self.IP = IP
        self.PORT = PORT

    def connect(self):
        self.client.connect((self.IP, self.PORT))

    def interractive(self):
        while True:
            cmd = input("ftp> ").strip()
            if len(cmd)==0:continue
            self.client.send(cmd.encode('utf-8'))
            print(self.client.recv(1024))


if __name__ == '__main__':
    print('FTP登录'.center(30, '-'))
    # IP = input("IP>>>").strip()
    # PORT = input("PORT>>>").strip()
    IP, PORT = '127.0.0.1', 9999
    ftp = FtpCient(IP, PORT)
    ftp.connect()
    ftp.interractive()


