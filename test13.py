# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/13 3:14 下午
# file: test13.py
# IDE: PyCharm


def calculate(x, n):
    if n == 0:
        return 1
    s = 1
    for i in range(n):
        s = s*x
    return s


def calculate1(x, n):
    if n == 0:
        return 1
    else:
        return x*calculate1(x, n-1)


if __name__ == '__main__':
    x = 3
    n = 4
    print(calculate1(x, n))
