from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # *** Blueprints ***
    from app.main import main
    app.register_blueprint(main)

    return app
