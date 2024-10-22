from app.models.device import Device


class DeviceService:
    @staticmethod
    def add_device(data, user_id=None):
        Device.add_device(data)

    @staticmethod
    def get_all_devices(user_id=None):
        # 如果提供 user_id，则仅获取该用户的设备
        if user_id:
            return Device.get_by_user_id(user_id)
        return Device.get_all()
