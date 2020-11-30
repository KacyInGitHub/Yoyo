# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/27 5:46 下午
# file: urls.py
# IDE: PyCharm

from .views import *

lg.add_url_rule('/d', view_func=Login.as_view('loginfunc'))
