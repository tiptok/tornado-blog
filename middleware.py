class MiddleWare(object):
    def process_request(self, handler):
        pass

    def process_response(self, handler):
        pass


class LogIntercept(MiddleWare):
    def log(self, handler):
        print("log before:",handler)

    def process_request(self, handler):
        self.log(handler)

class ResponseIntercept(MiddleWare):
    def log(self, handler):
        print("log after:",handler)

    def process_request(self, handler):
        self.log(handler)

def middlewares():
    return (LogIntercept(),ResponseIntercept() )