from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
from application import routes

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)

from application import routes