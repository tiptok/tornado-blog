#!/usr/bin/env python
# coding=utf8

from tornado.options import define, options
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.ioloop import IOLoop
from routers  import rules
from middleware import  middlewares
import logging
from lib.log import initlogger,InterceptHandler,logger

define(name="addr", default="127.0.0.1", metavar="http listen address")
define(name="port", default=8080, metavar="http listen port(8080)")
define(name="cmd", default="runserver", metavar="runserver")

class TornadoApplication(Application):
    def __init__(self):
        Application.__init__(self, rules) 

def httpserver():
    mids= middlewares
    server = HTTPServer(TornadoApplication(),xheaders=True)
    server.listen(options.port)
    IOLoop.current().start()

# 使用 loguru 替换 logging
logging.basicConfig(handlers=[InterceptHandler()], level=0)

if __name__ == "__main__":
    options.parse_command_line()
    initlogger()
    logger.debug((f"listen on %s:%d" % (options.addr,options.port)))
    if options.cmd == "runserver":
        httpserver()
    else:
        logger.debug("server stop")
