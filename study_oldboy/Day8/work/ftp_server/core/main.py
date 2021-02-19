#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-2-18 14:17
# @Author  : liuyang
# @File    : ftp_server.py
# @Software: PyCharm


import socketserver
import json
import configparser
import os
from conf import settings
from core import logger

class MyTCPHandler(socketserver.BaseRequestHandler):

    def auth(self, *args):
        """通过configparser模块实现用户认证，认证成功返回CODE201，失败放回CODE401"""
        username = args[0]['username']
        password = args[0]['passwd']
        auth_flag = False
        config_file = settings.DB_FILE

        if os.path.exists(config_file):
            config = configparser.ConfigParser()
            config.read(config_file)
            if username == config[username]['username'] and password == config[username]['password']:
                auth_flag=True
                if config[username].get('max_size'):
                    MAX_SIZE = config[username]['max_size']
                else:
                    MAX_SIZE = settings.DEFAULT_MAX_SIZE
                user_dic = {
                    'AUTH_CODE': 201,
                    'ROOT_PATH': os.path.join(settings.ROOT_PATH, username),
                    'CURRENT_PATH': os.path.join(settings.ROOT_PATH, username),
                    'MAX_SIZE': MAX_SIZE
                }
        if auth_flag:
            self.request.send(json.dumps(user_dic).encode("utf-8"))
            logger.logger('INFO','%s用户认证成功。' % username)
        else:
            user_dic = {
                'AUTH_CODE': 401
            }
            self.request.send(json.dumps(user_dic).encode("utf-8"))
            logger.logger('INFO','%s用户认证失败。' % username)

    def ls(self, *args):
        ls_dir = args[0]['ls_dir']
        res_dic = {}
        if not os.path.exists(ls_dir):
            res_dic['flag'] = False
            res_dic['info'] = "%s目录不存在" % ls_dir
            logger.logger('INFO', '%s目录不存在，ls失败。' % ls_dir)
        else:
            list_dir = os.listdir(ls_dir)
            res_dic['flag'] = True
            res_dic['list_dir'] = list_dir
        self.request.send(json.dumps(res_dic).encode("utf-8"))
        logger.logger('INFO', '%s目录ls成功。' % ls_dir)

    def mkdir(self, *args):
        mk_dir = args[0]['mk_dir']
        res_dic = {}
        if os.path.exists(mk_dir):
            res_dic['flag'] = False
            res_dic['info'] = "%s目录已经存在" % mk_dir
            logger.logger('INFO', '%s目录存在，mkdir失败。' % mk_dir)
        else:
            os.mkdir(mk_dir)
            res_dic['flag'] = True
        self.request.send(json.dumps(res_dic).encode("utf-8"))
        logger.logger('INFO', '%s目录mkdir成功。' % mk_dir)

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).decode("utf-8")
                print("%s wrote:" % self.client_address[0])
                cmd_dic = json.loads(self.data)
                print(cmd_dic)
                action = cmd_dic['action']
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(cmd_dic)
            except ConnectionResetError as e:
                print("err",e)
                break

