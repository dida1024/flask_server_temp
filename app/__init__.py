from flask import Flask
from .extensions import mongo,jwt
from .routes import register_routes
from .utils.response import error_response
from .exceptions.custom_exceptions import CustomException
import logging


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # 初始化 MongoDB
    mongo.init_app(app)
    jwt.init_app(app)

    # 注册路由
    register_routes(app)

    # 自定义异常处理
    @app.errorhandler(CustomException)
    def handle_custom_exception(error):
        return error_response(message=error.message, status_code=error.status_code)

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        logging.error(f"Unhandled Exception: {error}")
        return error_response(message="Internal server error.", status_code=500)

    return app
