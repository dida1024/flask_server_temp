from marshmallow import Schema, ValidationError
from ..utils.logger import log


class BaseSchema(Schema):
    """基础Schema类"""

    @staticmethod
    def handle_error(error: ValidationError, data, **kwargs):
        """统一的错误处理"""
        # 构建错误信息
        error_details = {
            'messages': error.messages,
            'data': data
        }

        log.warning(
            f"Data validation failed: {error_details}",
            extra={'error_details': error_details}
        )
        return error.messages