import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import configparser

'''configuring the Flask App'''
app = Flask(__name__)
CORS(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# db config
config = configparser.ConfigParser()
try:
    config.read("app.conf")
    app.logger.info('config file available')
    app.config['SECRET_KEY'] = 'Pn327@ms9oY-L5'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
        config.get('DB', 'user') + ':' + \
        config.get('DB', 'password') + '@' + config.get('DB', 'host') + '/' + \
        config.get('DB', 'db')
except():
    app.logger.error("No config file present")


bcrypt = Bcrypt(app)
# initialize sql-alchemy
db = SQLAlchemy(app)

with app.app_context():
    from src.api.models import user_model, article, comment, section
    db.create_all()

app.run()
