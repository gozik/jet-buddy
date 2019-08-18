import os
from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'secret-password'
app.config['UPLOAD_FOLDER'] = os.path.join('.', 'uploads')

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models