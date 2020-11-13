# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/11 7:50 下午
# file: test1.py
# IDE: PyCharm


def num_statistic(num_list):
    i = 0
    j = 0
    if isinstance(num_list, list):
        for n in num_list:
            if n < 0:
                i += 1
            elif n > 0:
                j += 1
            else:
                pass
    return i, j
