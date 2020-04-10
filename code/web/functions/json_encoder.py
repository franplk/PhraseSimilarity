#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-03
# @Author Franplk

"""
自定义Json序列化编码
"""

from datetime import datetime, date
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return dict(obj)
