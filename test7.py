# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/11 8:16 下午
# file: test7.py
# IDE: PyCharm
import math


def find_shuixian_num(begin, end):
    res = []
    if begin <= end:
        for n in range(begin, end+1):
            tmp = 0
            n_tmp = n
            while n > 9:
                t = n % 10
                # tmp = tmp + t*t*t
                tmp = tmp + math.pow(t, 3)
                n = int(n / 10)
            tmp = tmp + n*n*n
            if tmp == n_tmp:
                res.append(n_tmp)
    return res


def find_shuixian_num1(begin, end):
    res = []
    if begin <= end:
        for n in range(begin, end+1):
            num_list = list(str(n))
            sum = 0
            for i in num_list:
                sum = sum + int(i)*int(i)*int(i)
            if sum == n:
                res.append(n)
    return res


def find_shuixian_num2(begin, end):
    sxh = []
    for i in range(begin, end):
        s = 0
        m = list(str(i))
        for j in m:
            s += int(j) ** len(m)
        if i == s:
            print(i)
            sxh.append(i)
    print("100-999 的水仙花数:%s" % sxh)


if __name__ == '__main__':
    begin = 100
    end = 999
    print(find_shuixian_num(begin, end))

