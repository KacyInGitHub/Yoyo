# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/13 3:01 下午
# file: test12.py
# IDE: PyCharm


def calculate(n):
    a = 1
    b = 1
    s = a + b
    l = [1, 1]
    while s < n:
        l.append(s)
        s = l[len(l)-1] + l[len(l)-2]

    return l


if __name__ == '__main__':
    n = 13
    print(calculate(n))