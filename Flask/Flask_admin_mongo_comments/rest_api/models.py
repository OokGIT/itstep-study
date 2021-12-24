# from datetime import datetime
from app import db


class Vendor(db.Document):
    name = db.StringField()

    def __str__(self):
        return f"{self.name}"


class Tag(db.Document):
    name = db.StringField()

    def __str__(self):
        return f"{self.name}"


class CPU(db.Document):
    name = db.StringField()
    price = db.DecimalField()
    freq = db.StringField()
    cache = db.StringField()
    vendor = db.ReferenceField(Vendor)
    tags = db.ListField(db.ReferenceField(Tag))
    # created_date_time = db.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.name}"

    def append_tag(self, name):
        tag = Tag.objects.filter(
            name__containts=name
        )
        if not tag:
            tag = Tag.objects.create(name=name)

        self.tags.append(str(tag.id))

        return self.tags

