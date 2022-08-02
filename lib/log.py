import logging

from loguru import logger

logger = logger

def initlogger():

    # formatter = logging.Formatter("[%(asctime)s  %(filename)s:%(funcName)s:%(lineno)s] [%(name)s] [%(levelname)s] %(message)s",datefmt='%Y-%d-%m %H:%M:%S')
    # streamHandler = logging.StreamHandler()
    # streamHandler.setFormatter(formatter)
    #
    # l = logging.getLogger('peewee')
    # l.addHandler(streamHandler)
    # l.setLevel(logging.DEBUG)
    # l.propagate = False

    # 启用peewee sql query log
    l = logging.getLogger('peewee')
    l.setLevel(logging.DEBUG)

class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )