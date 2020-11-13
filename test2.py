# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/11 7:55 下午
# file: test2.py
# IDE: PyCharm


def formate_str(origin_str):
    res = []
    for i, s in enumerate(origin_str):
        if i % 2 == 0:
            res.append(s)
    return "".join(res)


def formate_str1(origin_str):
    res = origin_str[::2]
    return res


if __name__ == '__main__':
    s = "axbyczdj"
    r = formate_str1(s)
    print(r)
