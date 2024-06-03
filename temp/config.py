import os


class Config(object):
    db_host = os.getenv("DB_HOST", "localhost")
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:123456@{db_host}:3306/erp?charset=utf8mb4'
    HOST = "0.0.0.0"
    PORT = os.getenv("LISTEN_PORT", "5000")
