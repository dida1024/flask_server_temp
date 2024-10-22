from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from ..exceptions.custom_exceptions import InvalidCredentials, UserAlreadyExists
from ..services.user_service import UserService
from ..utils.response import success_response, error_response

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return error_response("Username and password are required.", 400)

    try:
        UserService.register(username, password)
        return success_response(message="User registered successfully.")
    except UserAlreadyExists as e:
        return error_response(message=str(e), status_code=400)


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    try:
        # 验证用户并登录
        access_token = UserService.login(username, password)
        return success_response(data={"access_token": access_token}, message="Login successful.")
    except InvalidCredentials as e:
        return error_response(message=str(e), status_code=401)


@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # JWT 是无状态的，不需要处理登出逻辑
    return success_response(message="Logout successful.")
