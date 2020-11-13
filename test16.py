# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/13 4:45 下午
# file: test16.py
# IDE: PyCharm
import os


def get_files(path=os.path.dirname(__file__), rule=".py"):
    file_list = []
    for fpath, dirs, fs in os.walk(path):
        for f in fs:
            file_name = os.path.join(fpath, f)
            if file_name.endswith(rule):
                file_list.append(file_name)
    return file_list


if __name__ == '__main__':
    res = get_files(os.path.dirname(__file__))
    print(res)
