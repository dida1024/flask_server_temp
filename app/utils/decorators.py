from functools import wraps
from marshmallow import ValidationError
from ..exceptions.custom_exceptions import CustomException
from ..utils.response import error_response
from ..utils.logger import log

def handle_exceptions(error_messages=None):
    """
    异常处理装饰器
    Args:
        error_messages: 可选的自定义错误消息映射
    """
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            try:
                return f(*args, **kwargs)
                
            except ValidationError as e:
                log.warning(f"Validation error: {e.messages}")
                return error_response(
                    message=error_messages.get('validation_error', e.messages) if error_messages else e.messages,
                    status_code=400
                )
                
            except CustomException as e:
                return error_response(message=str(e), status_code=e.status_code)
                
            except Exception as e:
                log.error(f"Unexpected error: {str(e)}", exc_info=True)
                return error_response(message="Service error", status_code=500)
                
        return decorated
    return decorator