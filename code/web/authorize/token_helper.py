#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-11
# @Author Franplk

from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer


class TokenHelper(object):
    default_salt = '2020.03.11'
    token_generator = TimedJSONWebSignatureSerializer(default_salt, expires_in=3600)

    @classmethod
    def generate_token(cls, params_obj, salt=None):
        if salt is None:
            salt = cls.default_salt
        token = cls.token_generator.dumps(params_obj, salt=salt)
        return token.decode()

    @classmethod
    def verify_token(cls, token, salt=None):
        verify_result = {
            'code': 200, 'message': 'OK'
        }
        try:
            source = cls.token_generator.loads(token, salt=salt)
            verify_result['data'] = source
        except SignatureExpired:
            verify_result['code'] = 100,
            verify_result['message'] = 'Token已过期',
        except BadSignature:
            verify_result['code'] = 100,
            verify_result['message'] = 'Token无效',
        return verify_result


if __name__ == '__main__':
    token_params = {
        'id': 2, 'name': '测试模型二'
    }
    # 生成Token
    token_obj_1 = TokenHelper.generate_token(token_params)
    import time
    time.sleep(5)
    # 第二次生成与第一次生成的Token不同
    token_obj_2 = TokenHelper.generate_token(token_params)
    print('token1 = {}'.format(token_obj_1))
    print('token2 = {}'.format(token_obj_2))
    # 验证Token
    params_source_1 = TokenHelper.verify_token(token_obj_1)
    print('验证后params-1 = {}'.format(params_source_1))
    params_source_2 = TokenHelper.verify_token(token_obj_2)
    print('验证后params-2 = {}'.format(params_source_2))
