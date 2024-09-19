from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config  # we’ll discuss the config file next

db = SQLAlchemy()

def create_app(config_name):
    # Create flask application
    # It determines the root directory for the application.
    app = Flask(__name__)
    # Load Configuration
    # Loading the config setting by config[config_name]
    # The configuration are impoted from the config module
    app.config.from_object(config[config_name])
    # Initialize Configuration
    # It calls the init_app
    config[config_name].init_app(app)
    # Loading additional configuration
    # This allows for further customization of the application
    app.config.from_pyfile("../config.py")
    # Initialize SQLAlchemy
    # Database Instance 
    db.init_app(app)
    # Register Blueprint 
    # The blueprint is registered with a URL prefix of /api/, meaning all routes defined in the api blueprint will be prefixed with /api/.
    from .api import api as api_blueprint  # We will discuss blueprints shortly as well
    app.register_blueprint(api_blueprint, url_prefix='/api/')
    # COnfigured flask application
    return app