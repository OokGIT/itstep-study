import random

names = ['Иван', 'Петр', 'Василий', 'Геннадий']
surnames = ['Данилов', 'Ефремов', 'Гончаренко', 'Мартыненко', 'Стругацкий']
cities = ['Киев', 'Одесса', 'Ереван', 'Херсон']

print("Длина стартового списка:", len(names))

users_db_item = dict()
users_db = dict()

for i in range(len(names)):
    users_db_item['name'] = random.choice(names)
    users_db_item['surname'] = random.choice(surnames)
    users_db_item['age'] = random.randrange(18, 56)
    users_db_item['city'] = random.choice(cities)
    users_db_item['user_id'] = hash(random.randrange(1, 52595))
    users_db[i] = users_db_item
    print(i)
    print(users_db[i])


