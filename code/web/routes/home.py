#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-04-09
# @Author Franplk

from flask import Blueprint, current_app

from web.helper import WebHelper

route_home = Blueprint('home_page', __name__)


@route_home.route("/")
def index():
    return WebHelper.page_render("index")


@route_home.route("/welcome")
def welcome():
    return WebHelper.page_render("welcome")


@route_home.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('favicon.ico')
