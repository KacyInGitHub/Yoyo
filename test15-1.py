# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/13 5:48 下午
# file: test15-1.py
# IDE: PyCharm
import re


def is_mail_style(x):
    a = re.match(r'^[0-9a-zA-Z_\-]+@[0-9a-zA-Z]+(\.com)$', x)
    if a:
        yhm = re.findall("^(.+?)@", x)
        print(f"用户名:{yhm[0]}")
        gc = re.findall("@(.+?)\.com", x)
        print(f"公司名:{gc[0]}")
        return True
    else:
        print("incorrect email format")
        return False


if __name__ == '__main__':
    a = input("请输入: ")
    while 1:
        if a == "q" or a == "Q":
            exit()
        else:
            if is_mail_style(a):
                pass
            a = input("请输入: ")
