from app import create_app
from app.utils.logger import setup_logger

app = create_app()
logger = setup_logger(app)

if __name__ == '__main__':
    app.run(debug=True)
