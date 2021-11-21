from datetime import datetime
from app import db


class User(db.Document):
    name = db.StringField()
    last_name = db.StringField()
    created_date_time = db.DateTimeField(default=datetime.now)
