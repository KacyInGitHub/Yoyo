# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/12 10:24 上午
# file: test8.py
# IDE: PyCharm


def find_perfect_num(num):
    res = []
    for i in range(1, num+1):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s = s + j
        if s == i:
            res.append(i)
    return res


def find_perfect_num1(num):
    a = []
    for i in range(1, 1000):
        s = 0
        for j in range(1, i):
            if i % j == 0 and j < i:
                s += j
        if s == i:
            a.append(i)
    return a


if __name__ == '__main__':
    num = 1000
    print(find_perfect_num(num))