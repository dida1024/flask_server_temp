import os


class Config:
    JWT_SECRET_KEY = 'your_secret_key'  # 设置一个强随机字符串
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/iot_db')  # 替换为你的 MongoDB URI
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')  # 日志级别
