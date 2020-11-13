# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/13 2:39 下午
# file: test10.py
# IDE: PyCharm
import test9


def sort_normal(l):
    # return test9.bubble_sort(l)
    l.sort()
    return l


def sort_invert(l):
    # return test9.bubble_sort(l)[::-1]
    l.sort(reverse=True)
    return l


def sort_unsame(l):
    return list(set(l))


if __name__ == '__main__':
    l = [10,9,6,7,3,2,1,4,5,8]
    print(sort_normal(l))
    print(sort_invert(l))
    print(sort_unsame(l))