#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-18 14:29
# @Author  : liuyang
# @File    : ftp_client.py
# @Software: PyCharm

import socket
import getpass
import json
import os

class FtpCient(object):
    def __init__(self, IP, PORT):
        self.client = socket.socket()
        self.IP = IP
        self.PORT = PORT

    def connect(self):
        self.client.connect((self.IP, self.PORT))

    def help(self, *args):
        msg = """Commands may be abbreviated.  Commands are:
        ls
        pwd
        cd ../..
        mkdir dirname
        rmdir dirname
        rm  filename
        get filename
        put filename
        exit
        """
        print(msg)
        if args:
            user_dic = args[1]
            return user_dic

    def user_auth(self):
        """用户登录认证"""
        username = input('username>>>').strip()
        # passwd = getpass.getpass('password>>>')   # getpass在pycharm中不好用，可以用cmd环境试验
        passwd = input('password>>>').strip()
        msg_dic = {
            "action": "auth",
            "username": username,
            "passwd": passwd
        }
        self.client.send(json.dumps(msg_dic).encode("utf-8"))
        user_dic = json.loads(self.client.recv(1024).decode())
        return user_dic

    def ls(self, *args):
        user_dic = args[1]
        if len(args[0].split()) == 1:
            ls_dir = user_dic['CURRENT_PATH']
        else:
            ls_dir = os.path.join(user_dic['CURRENT_PATH'], args[0].split()[1])
        msg_dic = {
            'action': 'ls',
            'ls_dir': ls_dir
        }
        self.client.send(json.dumps(msg_dic).encode("utf-8"))
        res_dic = json.loads(self.client.recv(1024))
        if not res_dic['flag']:
            print(res_dic['info'])
        else:
            for l in res_dic['list_dir']:
                print(l, end='\t')
            print('')
        return user_dic


    def pwd(self, *args):
        user_dic = args[1]
        pwd_dir = user_dic['CURRENT_PATH']
        print(pwd_dir)
        return user_dic

    def cd(self, *args):
        """切换目录，还未完全实现"""
        user_dic = args[1]
        user_dic['CURRENT_PATH'] = os.path.join(user_dic['CURRENT_PATH'], args[0].split()[1])
        return user_dic

    def mkdir(self, *args):
        user_dic = args[1]
        if len(args[0].split()) == 1:
            self.help()
        else:
            mk_dir = os.path.join(user_dic['CURRENT_PATH'], args[0].split()[1])
            msg_dic = {
                'action': 'mkdir',
                'mk_dir': mk_dir
            }
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            res_dic = json.loads(self.client.recv(1024))
            if not res_dic['flag']:print(res_dic['info'])
        return user_dic

    def put(self, *args):
        print(args)
        user_dic = args[1]
        return user_dic

    def exit(self, *args):
        exit("221 Goodbye.")


    def interractive(self):
        user_dic = self.user_auth()
        if user_dic['AUTH_CODE'] != 201:exit("用户或者密码不正常！")   # ftp用户认证
        while True:
            print(user_dic)
            cmd = input("ftp> ").strip()
            if len(cmd)==0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self, "%s" % cmd_str):
                func = getattr(self, "%s" % cmd_str)
                user_dic = func(cmd, user_dic)
            else:
                user_dic = self.help(cmd, user_dic)

if __name__ == '__main__':
    print('FTP登录'.center(30, '-'))
    # IP = input("IP>>>").strip()
    # PORT = input("PORT>>>").strip()
    IP, PORT = '127.0.0.1', 9999
    ftp = FtpCient(IP, PORT)
    ftp.connect()
    ftp.interractive()
