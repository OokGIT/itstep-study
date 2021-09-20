from class_UserList import UserList
# import random


My_App = UserList()


def get_choice():
    print('Here we can:\n', '- 1 Get users list\n', '- 2 Add new user\n',
          '- 3 Change user\n', '- 4 Delete user\n', '- 5 Search user\n',
          '- 6 Put users list to Excel')
    while True:
        get_number = int(input('Chose an action from 1 to 6... '))
        if get_number in range(1, 6):
            print('Ok,', get_number, 'selected')
            return get_number


if get_choice() == 1:
    print('---------- User List ----------')
    My_App.get_users()
elif get_choice() == 2:
    My_App.add_user()
elif get_choice() == 3:
    My_App.change_user()
elif get_choice() == 4:
    My_App.del_user()
elif get_choice() == 5:
    My_App.search_user()

# Print users list (task 1)
# for i in range(len(users_list)):
#     user_item = users_list[i]
#     for key, value in user_item.items():
#         print(key, user_item[key])
#     print('------------------')

# Add user to list (task 2)
# using list.append
# new_user = dict()
# new_user['user_id'] = str(hash(random.randrange(1, 52595)))
# new_user['name'] = input('Имя пользователя:')
# new_user['lastname'] = input('Фамилия пользователя:')
# new_user['age'] = input('Возраст:')
# new_user['city'] = input('Город:')
# users_list.append(dict(new_user))
# print(users_list)

# Change user (task 3)
# new_item = int(input('Выберите по какому полю ищем пользователя(цифра от 1 до'
#                      ' 5): 1-ID, 2-Имя, 3-Фамилия, 4-Возраст, 5-Город... '))
# if new_item == 1:
#     new_item_search = 'user_id'
# elif new_item == 2:
#     new_item_search = 'name'
# elif new_item == 3:
#     new_item_search = 'lastname'
# elif new_item == 4:
#     new_item_search = 'age'
# elif new_item == 5:
#     new_item_search = 'city'
# else:
#     print('Неверный выбор')
# search_value = input(f'Введите искомое значение для'
#                      f' выбранного поля {new_item_search}... ')
# for i in range(len(users_list)):
#     user_item = users_list[i]
#     for key, value in user_item.items():
#         if value == search_value:
#             print('По условию найдена запись:\n', user_item)
#             if input('Вносим изменения в данные этого пользователя? Y / N') == ('y' or 'Y'):
#                 new_value = input('Введите новое значение')
#                 user_item[key] = new_value
#                 print('Новое значение записи:', user_item)
#             else:
#                 print('Оставляем запись без изменения')

# Delete user (task 4)
# new_item = int(input('Выберите по какому полю ищем пользователя(цифра от 1 до'
#                      ' 5): 1-ID, 2-Имя, 3-Фамилия, 4-Возраст, 5-Город... '))
# if new_item == 1:
#     new_item_search = 'user_id'
# elif new_item == 2:
#     new_item_search = 'name'
# elif new_item == 3:
#     new_item_search = 'lastname'
# elif new_item == 4:
#     new_item_search = 'age'
# elif new_item == 5:
#     new_item_search = 'city'
# else:
#     print('Неверный выбор')
# search_value = input(f'Введите искомое значение для'
#                      f' выбранного поля {new_item_search}... ')
# for i in range(len(users_list)):
#     user_item = users_list[i]
#     for key, value in user_item.items():
#         if value == search_value:
#             print('По условию найдена запись:\n', user_item)
#             if input('Удаляем данного пользователя ? Y / N') == ('y' or 'Y'):
#                 # users_list = users_list.remove(user_item)
#                 del users_list[i]
#                 print('New users list:', users_list)
#             else:
#                 print('Оставляем запись без изменения')


# Search user (task 5)
# new_item = int(input('Выберите по какому полю ищем пользователя(цифра от 1 до'
#                      ' 5): 1-ID, 2-Имя, 3-Фамилия, 4-Возраст, 5-Город... '))
# if new_item == 1:
#     new_item_search = 'user_id'
# elif new_item == 2:
#     new_item_search = 'name'
# elif new_item == 3:
#     new_item_search = 'lastname'
# elif new_item == 4:
#     new_item_search = 'age'
# elif new_item == 5:
#     new_item_search = 'city'
# else:
#     print('Неверный выбор')
# search_value = input(f'Введите искомое значение для'
#                      f' выбранного поля {new_item_search}... ')
# for i in range(len(users_list)):
#     user_item = users_list[i]
#     for key, value in user_item.items():
#         if value == search_value:
#             print('По условию найдена запись:\n', user_item)
