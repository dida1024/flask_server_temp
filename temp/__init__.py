from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from temp.config import Config

app = Flask("erp")
db = SQLAlchemy()


def middleware_load(app):
    CORS(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


def create_app():
    global app

    app.config.from_object(Config)
    app = middleware_load(app)

    from erp.api import apis

    for item in apis:
        app.register_blueprint(item)

    return app
