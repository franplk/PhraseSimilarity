#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Franplk

"""WEB 响应的封装"""

from flask import jsonify


class WebHelper(object):

    @staticmethod
    def json_render(code=200, message='操作成功', data=None, wrapper=True):
        """数据请求渲染函数"""
        if data is None:
            data = []
        if wrapper:
            result = {'code': code, 'message': message, 'data': data}
        else:
            result = data
        return jsonify(result)
