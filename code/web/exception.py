#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-21
# @Author Franplk
#
# 异常处理

import traceback

from flask import jsonify


class APIError(Exception):
    """
    Data Request Exception
    """
    def __init__(self, code=100, message='接口访问异常'):
        self.message = message
        self.code = code

    def error_msg(self):
        msg = {
            'code': self.code, 'message': self.message
        }
        return msg


class ExceptionHandler(object):
    ERROR_FILE = 'error.txt'

    def __init__(self, app=None):
        self.status = False
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if self.status:
            return

        @app.errorhandler(APIError)
        def data_error(exp):
            return jsonify(exp.error_msg())

        @app.errorhandler(Exception)
        def global_error(exp):
            """其他未捕获处理的异常写入异常文件,然后交给Flask框架自动处理"""
            traceback.print_exc(file=open(self.ERROR_FILE, 'a+'))

