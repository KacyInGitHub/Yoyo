# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/13 2:52 下午
# file: test11.py
# IDE: PyCharm


def calculate(n):
    s = 1
    for i in range(1, n+1):
        s = s * i
    return s


def calculate1(n):
    if n == 1:
        return n
    else:
        return n * calculate1(n-1)


def calculate2(a):
    from functools import reduce
    b = reduce(lambda x, y: x*y, range(1, a+1))
    return b


if __name__ == '__main__':
    n = 10
    print(calculate1(n))
