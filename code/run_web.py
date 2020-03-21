#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Franplk

"""主程序入口"""

import sys

from flask_script import Manager
from flask_script import Server

from web.www import app

manager = Manager(app)
multi_server = Server(
    port=app.config['SERVER_PORT'],
    use_debugger=app.config['DEBUG'],
    threaded=True, host=app.config['HOST']
)
manager.add_command("runserver", multi_server)


if __name__ == '__main__':
    sys.exit(manager.run(default_command='runserver'))
