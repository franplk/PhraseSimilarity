#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Franplk
#
# 应用程序配置

from flask import Flask

from web.functions import UrlManager
from web.functions import CustomJSONEncoder


class Application(Flask):
    """
    Flask重新封装
    1. 加入自定义JSON序列化
    2. 根据环境读取配置文件
    """

    json_encoder = CustomJSONEncoder

    def __init__(self, import_name, template_folder, static_folder):
        super().__init__(import_name, template_folder=template_folder, static_folder=static_folder)
        # 配置文件读取
        self.config.from_json('config/base.json')
        run_env = self.config.get('RUN_ENV', 'local')
        self.config.from_json('config/{}/model.json'.format(run_env))
        self.config.from_json('config/{}/server.json'.format(run_env))
        # 注册模板函数
        self._url_manager()

    def _url_manager(self):
        """函数模板"""
        release_version = self.config.get('RELEASE_VERSION')
        UrlManager(self, version=release_version)


'''应用初始化'''
app = Application(__name__, 'resource/templates', 'resource/static')
