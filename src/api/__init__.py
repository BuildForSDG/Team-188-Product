import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

'''configuring the Flask App'''
app = Flask(__name__)
CORS(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
# initialize sql-alchemy
db = SQLAlchemy(app)