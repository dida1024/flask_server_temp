from ..models.user import User
from ..exceptions.custom_exceptions import UserAlreadyExists, InvalidCredentials
from flask_jwt_extended import create_access_token  # 导入 JWT 生成函数


class UserService:
    @staticmethod
    def register(username, password):
        if User.validate(username, password):
            raise UserAlreadyExists()

        User.create(username, password)

    @staticmethod
    def login(username, password):
        user = User.validate(username, password)
        if not user:
            raise InvalidCredentials()

        # 创建 JWT 访问令牌，身份可以是用户的 ID 或用户名
        access_token = create_access_token(identity=user['username'])
        return access_token  # 返回生成的 JWT 令牌

    @staticmethod
    def get_all_users():
        return User.get_all()
