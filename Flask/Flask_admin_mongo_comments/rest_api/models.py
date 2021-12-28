from datetime import datetime
from app import db
from mongoengine import DateTimeField


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
    path_img = db.StringField()
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

    @property
    def get_tags(self):
        str_ = ""
        for i in self.tags:
            str_ += f"-{i.name}  "
        return str_


class Comment(db.Document):
    text = db.StringField()
    item = db.ReferenceField(CPU)
    date_created = db.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.text}"
