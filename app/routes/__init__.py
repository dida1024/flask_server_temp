from flask import Flask


def register_routes(app: Flask):
    from .user_routes import user_bp
    from .device_routes import device_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(device_bp, url_prefix='/api/devices')
