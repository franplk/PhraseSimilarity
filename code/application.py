#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Franplk
#
# 应用程序配置

from flask import Flask


class Application(Flask):
    """
    Flask重新封装
    1. 加入自定义JSON序列化
    2. 根据环境读取配置文件
    """

    def __init__(self, import_name, template_folder, static_folder):
        super().__init__(import_name, template_folder=template_folder, static_folder=static_folder)
        self.config.from_json('config/server.json')
        self.config.from_json('config/model.json')


'''应用初始化'''
app = Application(__name__, 'templates', 'static')
