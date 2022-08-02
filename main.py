#!/usr/bin/env python
# coding=utf8

import logging
import argparse
from lib.log import initlogger, InterceptHandler, logger
from serve import app

parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--addr', '-a', help='http listen address',default='127.0.0.1')
parser.add_argument('--port', '-p', help='year 属性，非必要参数，但是有默认值', default=8080)
parser.add_argument('--cmd', '-c', help='body 属性，必要参数', default="runserver")
options = parser.parse_args()

# 使用 loguru 替换 logging
logging.basicConfig(handlers=[InterceptHandler()], level=0)

if __name__ == "__main__":
    initlogger()
    logger.debug((f"listen on %s:%d" % (options.addr,options.port)))
    if options.cmd == "runserver":
        app.run(host=options.addr,port=options.port,debug=False,load_dotenv=True)
    else:
        logger.debug("server stop")
