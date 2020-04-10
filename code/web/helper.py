#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Franplk

"""WEB 响应的封装"""

from flask import jsonify, render_template


class WebHelper(object):

    @staticmethod
    def page_render(name, base='/pages', **context):
        """页面渲染函数"""
        page_name = '{}/{}.html'.format(base, name)
        return render_template(page_name, **context)

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
