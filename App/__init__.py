from flask import Flask
from App.models import db
from App.config import Config



def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import routes as main_blueprint
    app.register_blueprint(main_blueprint)

    from .errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    return app


