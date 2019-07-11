#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# File    :   evaluation.py
# Time    :   2019/07/09 16:19:25
# Author  :   AbelChe
# Blog    :   https://www.abelche.com
# Email   :   abelche@qq.com, ac.yucheng@gmail.com


import random
import re
import time

import chardet
import requests


def get_title(url, request, Headers):
    orirequest = request
    r = request.post(url, headers=Headers)
    fencode = chardet.detect(r.content)
    html = r.content.decode(fencode["encoding"])
    title = re.findall(r"<img name=\"(.*?)\"", html)
    for _ in title:
        p = _.split("#@")
        payload = {
            "wjbm": p[0],
            "bpr": p[1],
            "pgnr": p[5],
            "oper": "wjShow",
            "wjmc": p[3],
            "bprm": p[1],
            "pgnrm": p[4],
            "pageSize": "20",
            "page": "1",
            "currentPage": "1",
            "pageNo": "",
        }
        skipToEvalution(
            request.post(
                "http://zhjw.dlnu.edu.cn/jxpgXsAction.do", data=payload, headers=Headers
            ),
            payload,
            orirequest,
            Headers,
        )


def skipToEvalution(request, payload, orirequest, Headers):
    Headers["Host"] = "zhjw.dlnu.edu.cn"
    Headers["Content-Length"] = "284"
    Headers["Cache-Control"] = "max-age=0"
    Headers["Origin"] = "http://zhjw.dlnu.edu.cn"
    Headers["Upgrade-Insecure-Requests"] = "1"
    Headers["Content-Type"] = "application/x-www-form-urlencoded"
    Headers[
        "Accept"
    ] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
    Headers["Referer"] = "http://zhjw.dlnu.edu.cn/jxpgXsAction.do"
    Headers["Accept-Encoding"] = "gzip, deflate"
    Headers["Accept-Language"] = "zh-CN,zh;q=0.9"
    Headers["Connection"] = "close"
    rlist = re.findall(
        r"<input type=\"radio\" name=\"(.*?)\"\s+value=\"(.*?)\"  id=", request.text
    )
    epayload = {
        "wjbm": payload["wjbm"],
        "bpr": payload["bpr"],
        "pgnr": payload["pgnr"],
        "zgpj": "1",
    }
    for i in rlist:
        if i[1][-1] == "1":
            epayload[i[0]] = i[1]
    # print(epayload)
    time.sleep(1)
    res = orirequest.post(
        "http://zhjw.dlnu.edu.cn/jxpgXsAction.do?oper=wjpg",
        data=epayload,
        headers=Headers,
    )
    # print(res.text, len(res.text))
    print("-------------------------------------------------------------------------")
    if res.text.find("评估成功") > 0:
        print("\t\t(成功)", payload["pgnrm"])
    else:
        print("\t\t(失败)", payload["pgnrm"])
    print("-------------------------------------------------------------------------")
