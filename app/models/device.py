from bson import ObjectId
from ..extensions import mongo
from .base_model import BaseModel
from typing import Optional, List
from datetime import datetime, timezone


class Device(BaseModel):
    name: str
    type: str
    user_id: str

    @staticmethod
    def add_device(device_data: dict) -> None:
        device_data["created_at"] = datetime.now(timezone.utc)
        device_data["updated_at"] = datetime.now(timezone.utc)
        mongo.db.devices.insert_one(device_data)

    @staticmethod
    def get_all() -> List[dict]:
        return list(mongo.db.devices.find())

    @staticmethod
    def get_by_id(device_id: str) -> Optional[dict]:
        return mongo.db.devices.find_one({"_id": ObjectId(device_id)})

    @staticmethod
    def get_by_user_id(user_id: str) -> List[dict]:
        return list(mongo.db.devices.find({"user_id": user_id}))

    @staticmethod
    def update_device(device_id: str, updates: dict) -> None:
        updates["updated_at"] = datetime.now(timezone.utc)
        mongo.db.devices.update_one(
            {"_id": ObjectId(device_id)},
            {"$set": updates}
        )

    @staticmethod
    def delete_device(device_id: str) -> None:
        mongo.db.devices.delete_one({"_id": ObjectId(device_id)})
