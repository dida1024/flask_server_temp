import logging
from flask import Flask


def setup_logger(app: Flask):
    logging.basicConfig(level=app.config['LOG_LEVEL'])
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler('app.log')
    handler.setLevel(app.config['LOG_LEVEL'])
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
