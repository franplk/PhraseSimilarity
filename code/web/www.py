#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-21
# @Author Franplk

from application import app
from web.exception import ExceptionHandler
from web.routes import route_api
from web.routes import route_page
from web.routes import route_home

'''蓝图路由配置'''
app.register_blueprint(route_home, url_prefix='/')
app.register_blueprint(route_api, url_prefix='/api')
app.register_blueprint(route_page, url_prefix='/page')

'''异常处理'''
handler = ExceptionHandler(app)
