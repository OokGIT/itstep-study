from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config.from_pyfile('./settings.py')
app.config.
