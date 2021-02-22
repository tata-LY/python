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
import sys
import re
from conf import settings
from core import logger
from core import common

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
            if username in config.sections():
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
            res_dic['info'] = "%s 目录不存在" % ls_dir
            logger.logger('INFO', '%s 目录不存在，ls失败。' % ls_dir)
        else:
            res_dic['flag'] = True
            if os.path.isdir(ls_dir):
                list_dir = os.listdir(ls_dir)
                res_dic['list_dir'] = list_dir
                logger.logger('INFO', '%s 目录ls成功。' % ls_dir)
            elif os.path.isfile(ls_dir):
                res_dic['list_dir'] = [ls_dir]
        self.request.send(json.dumps(res_dic).encode("utf-8"))

    def cd(self, *args):
        cd_dir = args[0]['cd_dir']
        root_path = args[0]['root_path']
        current_path = args[0]['current_path']
        res_dic = {}

        last_dir = os.getcwd()
        os.chdir(current_path)
        if os.path.exists(cd_dir) and os.path.isdir(cd_dir):
            os.chdir(cd_dir)
            pwd_dir = os.getcwd()
            if pwd_dir.startswith(root_path):
                """还在用户家目录下"""
                res_dic['flag'] = True
                res_dic['current_path'] = pwd_dir
                logger.logger('INFO', '切换到 %s 目录。' % cd_dir)
            else:
                """不在用户家目录下"""
                res_dic['flag'] = False
                res_dic['info'] = "进入 %s 目录权限不够" % cd_dir
                logger.logger('INFO', '进入 %s 目录权限不够。' % cd_dir)
            os.chdir(last_dir)
        else:
            res_dic['flag'] = False
            res_dic['info'] = "%s 目录不存在" % cd_dir
            logger.logger('INFO', '%s 目录不存在，cd失败。' % cd_dir)
        self.request.send(json.dumps(res_dic).encode("utf-8"))

    def mkdir(self, *args):
        mk_dir = args[0]['mk_dir']
        res_dic = {}
        if os.path.exists(mk_dir):
            res_dic['flag'] = False
            res_dic['info'] = "%s 目录已经存在" % mk_dir
            logger.logger('INFO', '%s 目录存在，mkdir失败。' % mk_dir)
        else:
            os.mkdir(mk_dir)
            res_dic['flag'] = True
            logger.logger('INFO', '%s 目录mkdir成功。' % mk_dir)
        self.request.send(json.dumps(res_dic).encode("utf-8"))

    def rmdir(self, *args):
        rmdir_dirname = args[0]['rmdir_dirname']
        res_dic = {}
        if not os.path.exists(rmdir_dirname):
            res_dic['flag'] = False
            res_dic['info'] = "%s不存在" % rmdir_dirname
            logger.logger('INFO', '%s 不存在，rm失败。' % rmdir_dirname)
        else:
            if os.path.isdir(rmdir_dirname):
                os.rmdir(rmdir_dirname)
                res_dic['flag'] = True
                logger.logger('INFO', '%s rm成功。' % rmdir_dirname)
            else:
                res_dic['flag'] = False
                res_dic['info'] = "%s 不是一个目录" % rmdir_dirname
                logger.logger('INFO', '%s 不是一个目录，rm失败。' % rmdir_dirname)
        self.request.send(json.dumps(res_dic).encode("utf-8"))

    def rm(self, *args):
        rm_filename = args[0]['rm_filename']
        res_dic = {}
        if not os.path.exists(rm_filename):
            res_dic['flag'] = False
            res_dic['info'] = "%s不存在" % rm_filename
            logger.logger('INFO', '%s不存在，rm失败。' % rm_filename)
        else:
            if os.path.isfile(rm_filename):
                os.remove(rm_filename)
                res_dic['flag'] = True
                logger.logger('INFO', '%s rm成功。' % rm_filename)
            else:
                res_dic['flag'] = False
                res_dic['info'] = "%s不是一个文件" % rm_filename
                logger.logger('INFO', '%s不是一个文件，rm失败。' % rm_filename)
        self.request.send(json.dumps(res_dic).encode("utf-8"))

    def put(self, *args):
        current_path = args[0]['current_path']
        filename = args[0]['filename']
        filesize = args[0]['filesize']
        max_size = args[0]['max_size']
        root_path = args[0]['ROOT_PATH']
        root_path_usage = common.dir_file_size(root_path)
        filename_abs = os.path.join(current_path, filename)
        res_dic['flag'] = True
        """判断是否有同名的目录存在"""
        if os.path.exists(filename) and os.path.isdir(filename):
            res_dic['flag'] = False
            res_dic['info'] = "上传的文件%s有同名的目录存在,上传失败" % filename
            logger.logger('INFO', "上传的文件%s有同名的目录存在,上传失败" % filename)
        """判断磁盘配额"""
        if max_size - root_path_usage < filesize:
            res_dic['flag'] = False
            res_dic['info'] = "空间不足,上传失败"
            logger.logger('INFO', "空间不足,上传失败")

        if res_dic['flag']:
            pass

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).decode("utf-8")
                if len(self.data) == 0:
                    break
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

