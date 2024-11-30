# app/schemas/user_schema.py

from marshmallow import Schema, fields, validate

from app.schemas.base import BaseSchema


class UserRegisterSchema(BaseSchema):
    username = fields.Str(
        required=True,
        validate=validate.Length(min=1),
        error_messages={
            "required": "Username is required.",  # 当未提供用户名时的错误消息
            "null": "Username cannot be null.",  # 当提供了 null 值时的错误消息
            "invalid": "Username must be a string."  # 当提供了无效类型时的错误消息
        }
    )
    password = fields.Str(
        required=True,
        load_only=True,
        error_messages={
            "required": "Password is required."  # 当未提供密码时的错误消息
        }
    )


class UserResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
