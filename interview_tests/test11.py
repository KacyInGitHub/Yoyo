# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/30 8:11 下午
# file: test11.py
# IDE: PyCharm

import threading
from threading import local
import time

obj = local()


def task(i):
    obj.xxxx = i
    time.sleep(2)
    print(f"{obj.xxxx}, {i}\n")


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task, args=(i,))
        t.start()
