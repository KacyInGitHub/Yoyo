# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/13 3:19 下午
# file: test14*****.py
# IDE: PyCharm


def han_nuo_ta(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        han_nuo_ta(n-1, a, c, b)
        print(a, '-->', c)
        han_nuo_ta(n-1, b, a, c)


if __name__ == '__main__':
    han_nuo_ta(5, "A", "B", "C")