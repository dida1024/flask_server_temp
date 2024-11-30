import logging
import os
from logging.handlers import RotatingFileHandler
from flask import current_app


def setup_logger(app=None):
    """设置日志系统
    Args:
        app: Flask应用实例（可选）
    """
    # 创建日志目录
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 创建日志记录器
    logger = logging.getLogger('app')
    logger.setLevel(logging.INFO)

    # 日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 文件处理器（按大小轮转）
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, 'app.log'),
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if app:
        app.logger = logger

    return logger


class Log:
    @staticmethod
    def info(message, *args, **kwargs):
        current_app.logger.info(message, *args, **kwargs)

    @staticmethod
    def error(message, *args, **kwargs):
        current_app.logger.error(message, *args, **kwargs)

    @staticmethod
    def warning(message, *args, **kwargs):
        current_app.logger.warning(message, *args, **kwargs)

    @staticmethod
    def debug(message, *args, **kwargs):
        current_app.logger.debug(message, *args, **kwargs)


# 创建全局实例
log = Log()