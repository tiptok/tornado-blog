from loguru import logger

class MiddleWare(object):
    def process_request(self, handler):
        pass

    def process_response(self, handler):
        pass


class LogIntercept(MiddleWare):
    def log(self, handler):
        logger.debug("log before recv:" + handler.request.uri)

    def process_request(self, handler):
        self.log(handler)
class ResponseIntercept(MiddleWare):
    def log(self, handler):
        logger.debug("log after",handler)

    def process_request(self, handler):
        # self.log(handler)
        pass
def middlewares():
    return (LogIntercept(),ResponseIntercept() )