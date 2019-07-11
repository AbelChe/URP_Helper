#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# File    :   login.py
# Time    :   2019/07/08 15:00:07
# Author  :   AbelChe
# Blog    :   https://www.abelche.com
# Email   :   abelche@qq.com, ac.yucheng@gmail.com


import getpass
import msvcrt
import random
import re
import sys

import chardet
import requests


def login(url, request, Headers):
    errorTime = 3
    while errorTime > 0:
        username = input("username: ")
        password = getpass.getpass("password: ")
        loginpayload = {"ldap": "auth", "zjh": username, "mm": password}
        r = request.post(url, data=loginpayload, headers=Headers)
        fencode = chardet.detect(r.content)
        if len(r.content.decode(fencode["encoding"])) > 500:
            errorTime -= 1
            print("用户名或密码错误！")
        else:
            print("正在自动进行教学评估...")
            return
    exit("错误次数过多，已退出")
