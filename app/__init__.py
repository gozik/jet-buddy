import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-password'
app.config['UPLOAD_FOLDER'] = os.path.join('.', 'uploads')

from app import routes