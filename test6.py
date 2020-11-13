# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/11 8:14 下午
# file: test6.py
# IDE: PyCharm


def exchange_value(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b


def exchange_value1(a, b):
    a, b = b, a
    return a, b


if __name__ == '__main__':
    a = 8
    b = 9
    print(exchange_value1(a, b))