import logging

from temp import create_app, db

app = create_app()
app.logger.setLevel(logging.INFO)

gunicorn_logger = logging.getLogger("gunicorn.error")
if gunicorn_logger:
    gunicorn_logger.setLevel(logging.INFO)
    app.logger.handlers = gunicorn_logger.handlers
