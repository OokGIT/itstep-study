from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine


# app config
app = Flask(__name__)
app.config.from_pyfile('settings.py')

# DB config
db = MongoEngine(app)

# Flask Admin config
admin = Admin(
    app,
    name='TEST',
    template_mode='bootstrap3',
)

# import rest_api.views
