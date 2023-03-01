from flask import Flask
from .config.config import config

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from flaskr.views.health import health
    
    app.register_blueprint(health)

    return app