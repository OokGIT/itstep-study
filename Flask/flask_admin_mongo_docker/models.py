# from datetime import datetime
from Flask.flask_admin_mongo_docker.app import db


class CPU(db.Document):
    name = db.StringField()
    price = db.DecimalField()
    freq = db.StringField()
    cache = db.StringField()
    # created_date_time = db.DateTimeField(default=datetime.now)
