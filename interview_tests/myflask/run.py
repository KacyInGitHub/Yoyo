# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/27 5:50 下午
# file: run.py
# IDE: PyCharm

from flask import Flask
from interview_tests.myflask.login import lg


app = Flask(__name__)

app.register_blueprint(lg, url_prefix='/login')

if __name__ == '__main__':
    app.run()