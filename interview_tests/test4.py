# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/19 2:07 下午
# file: test4.py
# IDE: PyCharm

# closure


def outer():
    x = 10
    y = [4]

    def inner():
        nonlocal x  # 两种内函数修改外函数临时变量的办法：1、nonlocal修饰内函数使用的临时变量；2、外函数临时变量类型为可变类型
        x += 1
        print(x)
        y[0] += 1
        print(y[0])
    return inner


if __name__ == '__main__':
    d = outer()
    d()
    d()
    d1 = outer()
    d1()
    d1()
