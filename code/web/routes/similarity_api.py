#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-09
# @Author Franplk

from flask import Blueprint, request

from web.helper import WebHelper
from web.services import SimilarityService

route_api = Blueprint("route_api", __name__)


@route_api.route('/similarity/compare', methods=['GET', 'POST'])
def sim_compare():
    req_value = dict(request.values)
    sen1 = req_value.get('sen1', None)
    sen2 = req_value.get('sen2', None)
    similar = SimilarityService.compare(sen1, sen2)
    res_data = {
        'sen1': sen1, 'sen2': sen2, 'similar': similar
    }
    return WebHelper.json_render(data=res_data)


@route_api.route('/similarity/mutual', methods=['GET', 'POST'])
def sim_mutual():
    req_value = dict(request.values)
    mode = req_value.get('mode', 'map')
    sens = req_value.get('sens', '')
    result = SimilarityService.multi_compare(mode, sens)
    return WebHelper.json_render(data=result)
