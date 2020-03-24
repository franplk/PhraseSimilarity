#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-09
# @Author Franplk

from flask import Blueprint, request

from web.helper import WebHelper
from web.services import SimilarityService

route_api = Blueprint("api_page", __name__)


@route_api.route('/similarity/compare', methods=['GET', 'POST'])
def sim_compare():
    req_value = dict(request.values)
    sen1 = req_value.get('sen1', None)
    sen2 = req_value.get('sen2', None)
    result = SimilarityService.compare(sen1, sen2)
    return WebHelper.json_render(data=result)


@route_api.route('/similarity/mutual', methods=['GET', 'POST'])
def sim_map():
    req_value = dict(request.values)
    mode = req_value.get('mode', 'map')
    sens = req_value.get('sens', '')
    result = SimilarityService.multi_compare(mode, sens)
    return WebHelper.json_render(data=result)
