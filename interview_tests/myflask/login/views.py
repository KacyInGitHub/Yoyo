# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/27 5:42 下午
# file: views.py
# IDE: PyCharm

from flask.views import MethodView
from flask.blueprints import Blueprint

lg = Blueprint('lg', __name__)


class Login(MethodView):
    @staticmethod
    def get():
        return "Hi there!"
