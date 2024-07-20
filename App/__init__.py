from flask import Flask
from App.models import db
from App.config import Config



def create_app():
    # Create an instance of the Flask class
    app=Flask(__name__)

    # Load configuration from the Config class
    app.config.from_object(Config)

    # Initialize the database with the Flask app instance
    db.init_app(app)

    # Import and register the main routes blueprint
    from .routes import routes as main_blueprint
    app.register_blueprint(main_blueprint)

    # Import and register the error handlers blueprint
    from .errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    return app


