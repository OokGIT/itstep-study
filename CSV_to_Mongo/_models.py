from mongoengine import *
connect(host="mongodb://127.0.0.1:27017/csv_to_mongo")

class WriteToDb(Document):
    url = StringField(required=True, primary_key=True)
    intern_id = StringField(max_length=12)
    title = StringField()
    description = StringField()
    published_at_utc = DateTimeField()


    def __str__(self):
        return self.url
