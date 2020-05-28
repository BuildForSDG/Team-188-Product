from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name = "development"):
    '''configuring the Flask App'''
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app