from flask import jsonify
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def success_response(data=None, message='Success', status_code=200):
    """
    统一成功响应格式
    :param data: 返回的数据
    :param message: 返回的消息
    :param status_code: HTTP 状态码，默认200
    :return: JSON 响应
    """
    response = jsonify({
        'status': 'success',
        'message': message,
        'data': data
    })

    logger.info(f"Success Response: {response.get_data(as_text=True)}")  # 记录成功响应日志
    return response, status_code


def error_response(message='Error', status_code=400):
    """
    统一错误响应格式
    :param message: 错误消息
    :param status_code: HTTP 状态码，默认400
    :return: JSON 响应
    """
    response = jsonify({
        'status': 'error',
        'message': message,
        'data': None
    })

    logger.error(f"Error Response: {response.get_data(as_text=True)}")  # 记录错误响应日志
    return response, status_code
