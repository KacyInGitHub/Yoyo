# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/19 4:04 下午
# file: test6.py
# IDE: PyCharm
import os


def get_upper_letters(file):
    count = 0
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            for letter in line:
               if letter.isupper():
                    count += 1
            line = f.readline()

    return count


def get_upper_letters1(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            for l in line:
                if l.isupper():
                    count += 1
    return count


def get_upper_letters2(file):
    count = 0
    with open(file, 'r') as f:
        data = f.read()
        for l in data:
            if l.isupper():
                count += 1
    return count


if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), 'letter_file.txt')
    print(get_upper_letters(file_path))