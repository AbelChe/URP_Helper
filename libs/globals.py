#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# File    :   global.py
# Time    :   2019/07/11 16:00:31
# Author  :   AbelChe
# Blog    :   https://www.abelche.com
# Email   :   abelche@qq.com, ac.yucheng@gmail.com


def statement():
    print(
        "####################################################\n"
        + "# Author  :   AbelChe                              #\n"
        + "# Blog    :   https://www.abelche.com              #\n"
        + "# QQ      :   305790018                            #\n"
        + '# Email   :   abelche@qq.com, ac.yucheng@gmail.com #\n'
        + "####################################################\n\n"
        + "----------------------------------------------------\n"
        + "       使用本软件造成的一切后果由使用者本人承担！       \n"
        + "                                                    \n"
        + "               同意(Y)       拒绝(N)                 \n"
        + "----------------------------------------------------"
    )
    judge = input("(Y/N):")
    if judge == "Y" or judge == "":
        print("欢迎使用")
    else:
        exit("再见")


def goodbye():
    print(
        '===========================================================\n'
        + '=                   THANK YOU FOR USING                   =\n'
        + '===========================================================\n'
    )