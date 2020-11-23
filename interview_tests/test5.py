# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/19 3:44 下午
# file: test5.py
# IDE: PyCharm


def test(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def test1(*args):
    for i in args:
        print(i)


if __name__ == '__main__':
    test(a=1, b=2, c=3)
    test1(1, 2, 3)
