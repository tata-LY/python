#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-3-5 10:13
# @Author  : liuyang
# @File    : ftp_client.py
# @Software: PyCharm

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
import hashlib
import sys
import math

def progressbar(cur, total):
    """进度条"""
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' % ('=' * int(math.floor(cur * 50 / total)), percent))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')

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
exit"""
        print(msg)
        if args:
            user_dic = args[1]
            return user_dic

    def user_auth(self):
        """用户登录认证"""
        username = input('username>>>').strip()
        # # passwd = getpass.getpass('password>>>')   # getpass在pycharm中不好用，可以用cmd环境试验
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
            else:
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
        if len(args[0].split()) == 1:
            user_dic['CURRENT_PATH'] = user_dic['ROOT_PATH']
        else:
            cd_dir = args[0].split()[1]
            msg_dic = {
                'action': 'cd',
                'root_path': user_dic['ROOT_PATH'],
                'current_path': user_dic['CURRENT_PATH'],
                'cd_dir': cd_dir
            }
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            res_dic = json.loads(self.client.recv(1024))
            if not res_dic['flag']:
                print(res_dic['info'])
            else:
                user_dic['CURRENT_PATH'] = res_dic['current_path']
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

    def rmdir(self, *args):
        """删除目录"""
        user_dic = args[1]
        if len(args[0].split()) == 1:
            self.help()
        else:
            rmdir_dirname = os.path.join(user_dic['CURRENT_PATH'], args[0].split()[1])
            msg_dic = {
                'action': 'rmdir',
                'rmdir_dirname': rmdir_dirname
            }
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            res_dic = json.loads(self.client.recv(1024))
            if not res_dic['flag']:print(res_dic['info'])
        return user_dic

    def rm(self, *args):
        """删除文件"""
        user_dic = args[1]
        if len(args[0].split()) == 1:
            self.help()
        else:
            rm_filename = os.path.join(user_dic['CURRENT_PATH'], args[0].split()[1])
            msg_dic = {
                'action': 'rm',
                'rm_filename': rm_filename
            }
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            res_dic = json.loads(self.client.recv(1024))
            if not res_dic['flag']:print(res_dic['info'])
        return user_dic

    def get(self, *args):
        user_dic = args[1]
        if len(args[0].split()) == 1:
            self.help()
        else:
            filename = args[0].split()[1]
            msg_dic = {
                'action': 'get',
                'current_path': user_dic['CURRENT_PATH'],
                'filename': filename
            }
            self.client.send(json.dumps(msg_dic).encode("utf-8"))  # 发送get_filename信息给server
            res_dic = json.loads(self.client.recv(1024).decode("utf-8"))   # 接收server端判断file文件的结果

            if res_dic['flag']:     # 开始接收
                revice_size = 0
                filesize = res_dic['filesize']
                f_w = open(filename, 'wb')
                while revice_size < filesize:
                    data = self.client.recv(1024)
                    f_w.write(data)
                    revice_size += len(data)
                    progressbar(revice_size, filesize)      # 进度条
                else:
                    f_w.close()
            else:
                print(res_dic['info'])
        return user_dic

    def put(self, *args):
        user_dic = args[1]
        if len(args[0].split()) == 1:
            self.help()
        else:
            put_filename = args[0].split()[1]
            _, filename = os.path.split(put_filename)
            if os.path.exists(put_filename):
                if os.path.isfile(put_filename):
                    filesize = os.stat(put_filename).st_size
                    msg_dic = {
                        'action': 'put',
                        'current_path': user_dic['CURRENT_PATH'],
                        'filename': filename,
                        'filesize': filesize,
                        'max_size': user_dic['MAX_SIZE'],
                        'root_path': user_dic['ROOT_PATH']
                    }
                    self.client.send(json.dumps(msg_dic).encode("utf-8"))
                    res_dic = json.loads(self.client.recv(1024).decode())
                    if res_dic['flag']:     # server使用selectors，不允许多次recv
                        f_r = open(put_filename, 'rb')
                        cur_size = 0
                        for line in f_r:
                            self.client.send(line)
                            cur_size += len(line)
                            progressbar(cur_size, filesize)  # 进度条
                        else:
                            f_r.close()
                    else:
                        print(res_dic['info'])
                else:
                    self.help()
            else:
                print("文件不存在")
        return user_dic

    def exit(self, *args):
        exit("221 Goodbye.")

    def interractive(self):
        user_dic = self.user_auth()
        if user_dic['AUTH_CODE'] != 201:exit("用户或者密码不正常！")   # ftp用户认证
        while True:
            # print(user_dic)
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
