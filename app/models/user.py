from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import mongo
from .base_model import BaseModel
from typing import Optional, List, Dict
from datetime import datetime, timezone
from ..utils.pagination import Pagination  # 引入 Pagination 工具类
from ..exceptions.custom_exceptions import UserAlreadyExists, UserNotFound, InvalidCredentials  # 引入自定义异常


class User(BaseModel):
    username: str
    password: str  # 原密码，不直接存储

    @staticmethod
    def create(username: str, password: str) -> None:
        # 检查用户是否已存在
        if mongo.db.users.find_one({"username": username}):
            raise UserAlreadyExists()  # 用户已存在，抛出异常

        hashed_password = generate_password_hash(password)
        user_data = {
            "username": username,
            "password": hashed_password,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc),
        }
        mongo.db.users.insert_one(user_data)

    @staticmethod
    def validate(username: str, password: str) -> Optional[dict]:
        user = mongo.db.users.find_one({"username": username})
        if user and check_password_hash(user['password'], password):
            return user
        raise InvalidCredentials()  # 无效凭证，抛出异常

    @staticmethod
    def get_all(page: int = 1, per_page: int = 10) -> Dict[str, any]:
        # 计算跳过的数量
        skip = (page - 1) * per_page

        # 查询用户
        users = list(mongo.db.users.find().skip(skip).limit(per_page))

        # 获取总数
        total = mongo.db.users.count_documents({})

        # 使用 Pagination 工具类
        pagination = Pagination(users, total, page, per_page)

        return pagination.to_dict()

    @staticmethod
    def get_by_id(user_id: str) -> Optional[dict]:
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise UserNotFound()  # 用户未找到，抛出异常
        return user

    @staticmethod
    def update_password(user_id: str, new_password: str) -> None:
        hashed_password = generate_password_hash(new_password)
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"password": hashed_password, "updated_at": datetime.now(timezone.utc)}}
        )

    @staticmethod
    def delete_user(user_id: str) -> None:
        result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            raise UserNotFound()  # 如果没有删除任何用户，抛出异常
