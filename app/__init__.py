from flask import Flask, Blueprint

from .config import config_by_name
from app.controller.tictactoe_controller import viewpage;

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(viewpage)
    static = Blueprint('static', __name__, template_folder='static', url_prefix = '/static')
    app.register_blueprint(static)
    
    return app
