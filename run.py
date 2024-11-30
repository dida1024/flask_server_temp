from app import create_app
from app.config import Config
from app.utils.logger import setup_logger

app = create_app()
logger = setup_logger(app)

if __name__ == '__main__':
    app.run(debug=True,host=Config.HOST,port=Config.PORT)
