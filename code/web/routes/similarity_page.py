#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 语义分析

from flask import Blueprint

from web.helper import WebHelper

route_page = Blueprint('route_page', __name__)
path_page = '/pages'


@route_page.route('/introduce', methods=['GET'])
def api_introduce():
    return WebHelper.page_render("introduce")


@route_page.route('/similar', methods=['GET'])
def phrase_similarity():
    return WebHelper.page_render("similar")
