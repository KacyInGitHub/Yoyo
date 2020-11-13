# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/11 8:05 下午
# file: test5.py
# IDE: PyCharm


def formate_list(l):
    middle = []
    if isinstance(l, list):
        pre = l[0:1]
        middle = l[1:3]
        last = l[3:]
        middle.extend(pre)
        middle.extend(last)
    return middle


def formate_list1(l):
    if isinstance(l, list):
        l.insert(3, l[0])
    return l[1:]


if __name__ == '__main__':

    l = [1, 3, 5, 7]
    ll = formate_list1(l)
    print(ll)