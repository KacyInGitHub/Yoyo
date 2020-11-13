# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/11 7:59 下午
# file: test3.py
# IDE: PyCharm


def str_split(o_str):
    res = o_str.split("_")
    return res


if __name__ == '__main__':
    o_str = "hello_world_yoyo"
    print(str_split(o_str))