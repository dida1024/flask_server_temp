from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_login import LoginManager

mongo = PyMongo()
login_manager = LoginManager()
jwt = JWTManager()
