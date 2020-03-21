#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Franplk
"""
Token验证方式
"""

from flask_httpauth import HTTPTokenAuth

from web.authorize import TokenHelper
from web.exception import APIError

auth_token = HTTPTokenAuth()


@auth_token.verify_token
def do_verify(token):
    verify_result = TokenHelper.verify_token(token)
    if verify_result['code'] != 200:
        raise APIError(message=verify_result['message'])
    return True
