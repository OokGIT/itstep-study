from mongoengine import *
connect(host="mongodb://127.0.0.1:27017/Schools")


class Schools(Document):
    school_number = StringField(required=True, max_length=4)
    school_name = StringField(max_length=128)
    school_city = StringField(max_length=64)
    school_address = StringField(max_length=128)
    school_type = ListField()

    def __str__(self):
        return self.school_number


class Classes(Document):
    class_number = StringField(required=True, max_length=4)
    class_tutor = StringField(max_length=128)
    class_school = ReferenceField(Schools)

    def __str__(self):
        return self.class_number


class Students(Document):
    stud_name = StringField(required=True)
    stud_lastname = StringField(required=True)
    stud_birth = DateField()
    stud_school = ReferenceField(Schools)
    stud_class = ReferenceField(Classes)


