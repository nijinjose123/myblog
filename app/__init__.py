from flask_api import FlaskAPI


applicaton = FlaskAPI(__name__)


from app import routes
