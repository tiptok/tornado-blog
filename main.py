#!/usr/bin/env python
# coding=utf8

from tornado.options import define, options
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.ioloop import IOLoop
from routers  import rules

define(name="addr", default="127.0.0.1", metavar="http listen address")
define(name="port", default=8080, metavar="http listen port(8080)")
define(name="cmd", default="runserver", metavar="runserver")

class TornadoApplication(Application):
    def __init__(self):
        Application.__init__(self, rules) 

def httpserver():
    server = HTTPServer(TornadoApplication(),xheaders=True)
    server.listen(options.port)
    IOLoop.current().start()


def runserver():
    username = "tiptok"     # input("input user name:")
    print("%s run server :%d" % (username, options.port))
    httpserver()


if __name__ == "__main__":
    options.parse_command_line()
    print("address:", options.addr)
    print("port:", options.port)
    if options.cmd == "runserver":
        runserver()
    else:
        print("server stop")
