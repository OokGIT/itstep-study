from Mongo_Classes import *
from Define_Schools import *

class1a = Classes(class_number='1А', class_school=school01).save(cascade=True)
class1b = Classes(class_number='1Б', class_school=school01).save(cascade=True)
class2a = Classes(class_number='1A', class_school=school02).save(cascade=True)
class2b = Classes(class_number='1Б', class_school=school02).save(cascade=True)
class3a = Classes(class_number='1A', class_school=school06).save(cascade=True)
class3b = Classes(class_number='1Б', class_school=school06).save(cascade=True)

# class1a = Classes(class_number='1А', class_school=school02).update()
# class1b = Classes(class_number='1Б', class_school=school02).update()
# class2a = Classes(class_number='1A', class_school=school02).update()
# class2b = Classes(class_number='1Б', class_school=school02).update()
# class3a = Classes(class_number='1A', class_school=school02).update()
# class3b = Classes(class_number='1Б', class_school=school02).update()
# class4a = Classes(class_number='1A', class_school=school02).update()
#
# class1a = Classes(class_number='1А', class_school=school06).save()
# class1b = Classes(class_number='1Б', class_school=school06).save()
# class2a = Classes(class_number='1A', class_school=school06).save()
# class2b = Classes(class_number='1Б', class_school=school06).save()
# class3a = Classes(class_number='1A', class_school=school06).save()
# class3b = Classes(class_number='1Б', class_school=school06).save()
# class4a = Classes(class_number='1A', class_school=school06).save()
