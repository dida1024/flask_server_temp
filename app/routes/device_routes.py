from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.device_service import DeviceService
from ..utils.response import success_response, error_response

device_bp = Blueprint('device', __name__)


@device_bp.route('/', methods=['POST'])
@jwt_required()  # 使用 JWT 进行保护
def add_new_device():
    data = request.get_json()
    if not data:
        return error_response("No device data provided.", 400)

    # 获取当前用户身份信息
    current_user = get_jwt_identity()

    # 可根据当前用户执行设备添加操作，例如关联设备与用户
    DeviceService.add_device(data, user_id=current_user)  # 假设 add_device 支持 user_id
    return success_response(message="Device added successfully.")


@device_bp.route('/', methods=['GET'])
@jwt_required()  # 使用 JWT 进行保护
def get_devices():
    current_user = get_jwt_identity()
    devices = DeviceService.get_all_devices(user_id=current_user)  # 假设 get_all_devices 支持 user_id
    return success_response(data=devices)
