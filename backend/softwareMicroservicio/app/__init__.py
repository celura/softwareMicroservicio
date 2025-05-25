from flask import Flask
from app.routes import software_routes
from backend.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(software_routes, url_prefix='/software')

    return app