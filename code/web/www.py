#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-21
# @Author Franplk

from application import app
from web.api import route_api
from web.exception import ExceptionHandler


'''蓝图路由配置'''
app.register_blueprint(route_api, url_prefix='/api')

'''异常处理'''
handler = ExceptionHandler(app)
