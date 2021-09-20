import random

names = ['Иван', 'Петр', 'Василий', 'Геннадий']
lastnames = ['Данилов', 'Ефремов', 'Гончаренко', 'Мартыненко', 'Стругацкий']
cities = ['Киев', 'Одесса', 'Ереван', 'Херсон']

print("Длина стартового списка:", len(names))

users_db_item = dict()
users_db = list()

for i in range(len(names)):
    users_db_item['user_id'] = (random.randrange(1, 52595))
    users_db_item['name'] = random.choice(names)
    users_db_item['lastname'] = random.choice(lastnames)
    users_db_item['age'] = random.randrange(18, 56)
    users_db_item['city'] = random.choice(cities)
    users_db.append(users_db_item.copy())
print(users_db)
