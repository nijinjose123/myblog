from flask_api import FlaskAPI
from .config import Config


application = FlaskAPI(__name__)
application.config.from_object(Config)

from app import routes
