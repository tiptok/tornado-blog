from tornado.web import RequestHandler 
import json
from middleware  import middlewares

class BaseHandler(RequestHandler):
    def initialize(self, middleware):
        self.middleware = middleware

    def prepare(self):
        for middleware in self.middleware:
            middleware.process_request(self)
        if self.request.headers['Content-Type'] == 'application/json':
            self.args = json.loads(self.request.body)
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
    async def options(self):
        self.finish()

    def finish(self, chunk=None):
        super(BaseHandler, self).finish(chunk)