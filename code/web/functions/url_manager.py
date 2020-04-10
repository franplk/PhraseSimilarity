#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-03
# @Author Franplk

"""
web访问的URL管理
"""

import time

from flask import url_for


class UrlManager(object):

    def __init__(self, flask_app, version=None):
        self.version = version if version else "%s" % (int(time.time()))
        self.register(flask_app)

    def register(self, flask_app):
        flask_app.add_template_global(self._build_url, 'buildUrl')
        flask_app.add_template_global(self._build_static_url, 'buildStaticUrl')

    def _build_url(self, path):
        return path

    def _build_static_url(self, path):
        file_path = "{}?v={}".format(url_for('static', filename=path.strip('/')), self.version)
        return file_path
