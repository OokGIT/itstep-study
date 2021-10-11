from mongoengine import *
connect(host="mongodb://127.0.0.1:27017/csv_to_mongo")


class WriteToDb(Document):
    internal_id = StringField(max_length=12)
    title = StringField()
    description = StringField()
    url = StringField(required=True)
    published_utc = DateTimeField()
    site = StringField()

    def __str__(self):
        return self.url
