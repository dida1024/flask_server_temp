class CustomException(Exception):
    """自定义异常基类"""

    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class UserAlreadyExists(CustomException):
    """用户已存在异常"""

    def __init__(self, message="User already exists."):
        super().__init__(message, status_code=400)


class UserNotFound(CustomException):
    """用户未找到异常"""

    def __init__(self, message="User not found."):
        super().__init__(message, status_code=404)


class InvalidCredentials(CustomException):
    """无效凭据异常"""

    def __init__(self, message="Invalid username or password."):
        super().__init__(message, status_code=401)


class DeviceNotFound(CustomException):
    """设备未找到异常"""

    def __init__(self, message="Device not found."):
        super().__init__(message, status_code=404)
