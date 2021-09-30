from Mongo_Classes import *

# school10 = Schools(school_number='10').save()
# school20 = Schools(school_number='20').save()
# school30 = Schools(school_number='30').save()
# class01 = Classes(class_number='1A', class_school=school10).save()
# class02 = Classes(class_number='2A', class_school=school20).save()
# class03 = Classes(class_number='3A', class_school=school30).save()
# user01 = Students(stud_name='Иван', stud_lastname='Ефремов',
#                   stud_class=class02, stud_school=school20).save()
# user02 = Students(stud_name='Алла', stud_lastname='Гончарук',
#                   stud_class=class02, stud_school=school20).save()
# user03 = Students(stud_name='Михаил', stud_lastname='Карасевич',
#                   stud_class=class03, stud_school=school10).save()
# user04 = Students(stud_name='Василий', stud_lastname='Мухин',
#                   stud_class=class01, stud_school=school30).save()
# user05 = Students(stud_name='Ольга', stud_lastname='Махно',
#                   stud_class=class02, stud_school=school20).save()
# user06 = Students(stud_name='Кирилл', stud_lastname='Булкин',
#                   stud_class=class03, stud_school=school10).save()

for student in Students.objects:
    print(student.stud_name, student.stud_lastname, student.stud_school, student.stud_class)
