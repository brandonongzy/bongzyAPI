from flask import Flask
from flask_cors import CORS
from flask_cors import CORS
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    return app


app = create_app()
CORS(app)


def register_routes():
    from app.routes.weather import weather
    from app.routes.transport import transport

    app.register_blueprint(weather)
    app.register_blueprint(transport)


register_routes()
