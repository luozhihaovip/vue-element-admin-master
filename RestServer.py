#!/usr/bin/env python
# -*- coding:utf-8 -*-

import flask, json, logging
import connectMysql #引用ConnectMysql文件
from flask import request

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

server = flask.Flask(__name__)


@server.route('/v1/brd/task', methods=['post'])
def task():
    json_req = request.json
    logger.info("接受到参数：%s",json_req)

    successed = True
    message=''
    code = 200
    try:
        print('111111111')
    except:
        message = 'this is a exception message!'
        successed = False
        code = 500

    res = {'successed': successed,
           'message': message,
           'code': code
           }

    return json.dumps(res, ensure_ascii=False)


server.run(port=7777, debug=True, host='0.0.0.0')