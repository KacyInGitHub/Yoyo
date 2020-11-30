# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/27 5:28 下午
# file: test9.py
# IDE: PyCharm

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def login():
    data = request.args
    print(data)
    return f"Hello world, Hi {data.get('name')}"


if __name__ == '__main__':
    app.run()
