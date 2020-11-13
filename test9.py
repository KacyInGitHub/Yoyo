# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/12 10:33 上午
# file: test9.py
# IDE: PyCharm


def bubble_sort(l):
    if isinstance(l, list):
        for i in range(len(l)-1):
            for n in range(len(l)-1-i):
                if l[n] > l[n+1]:
                    l[n], l[n+1] = l[n+1], l[n]
    return l


if __name__ == '__main__':
    l = [10,9,6,7,3,2,1,4,5,8]
    r = bubble_sort(l)
    print(r)