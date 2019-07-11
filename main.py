#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# File    :   main.py
# Time    :   2019/07/09 16:19:15
# Author  :   AbelChe
# Blog    :   https://www.abelche.com
# Email   :   abelche@qq.com, ac.yucheng@gmail.com


import requests

import settings
from libs import globals
from models import evaluation, login

Host = settings.HOST
Headers = settings.HEADERS

if __name__ == "__main__":
    globals.statement()
    request = requests.Session()
    login.login(Host + "loginAction.do", request, Headers)
    evaluation.get_title(Host + "jxpgXsAction.do?oper=listWj", request, Headers)
    globals.goodbye()
