from mongoengine import *
connect(host="mongodb://127.0.0.1:27017/my_school")


class Schools(Document):
    school_number = StringField(required=True)

    def __str__(self):
        return self.school_number

class Classes(Document):
    class_name = StringField(required=True)
    class_school = ReferenceField(Schools)

    def __str__(self):
        return self.class_name


class Students(Document):
    stud_name = StringField(required=True)
    stud_lastname = StringField(required=True)
    class_name = ReferenceField(Classes)
    school_number = ReferenceField(Schools)


school10 = Schools(school_number='10').save()
school20 = Schools(school_number='20').save()
school30 = Schools(school_number='30').save()
class01 = Classes(class_name='1A', class_school=school10).save()
class02 = Classes(class_name='2A', class_school=school20).save()
class03 = Classes(class_name='3A', class_school=school30).save()
user01 = Students(stud_name='Иван', stud_lastname='Ефремов', class_name=class02, school_number=school20).save()
user02 = Students(stud_name='Алла', stud_lastname='Гончарук', class_name=class02, school_number=school20).save()
user03 = Students(stud_name='Михаил', stud_lastname='Карасевич', class_name=class03, school_number=school10).save()
user04 = Students(stud_name='Василий', stud_lastname='Мухин', class_name=class01, school_number=school30).save()

for student in Students.objects:
    print(student.stud_name, student.stud_lastname, student.class_name,
          student.school_number)
