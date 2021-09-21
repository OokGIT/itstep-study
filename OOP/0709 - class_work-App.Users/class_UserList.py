import random

from xlsxwriter import Workbook

users_list = [{'user_id': '18456', 'name': 'Артем', 'lastname': 'Данилов',
               'age': '44', 'city': 'Херсон'},
              {'user_id': '40385', 'name': 'Иван', 'lastname': 'Гончаренко',
               'age': '44', 'city': 'Ереван'},
              {'user_id': '33453', 'name': 'Олег', 'lastname': 'Денисенко',
               'age': '13', 'city': 'Киев'}
              ]


class UserList:

    def __init__(self):
        self.my_list = users_list

    def get_users(self):
        for i in range(len(self.my_list)):
            user_item = self.my_list[i]
            for key, value in user_item.items():
                print(key, user_item[key])
            print('------------------')

    def add_user(self):
        new_user = dict()
        new_user['user_id'] = str(hash(random.randrange(1, 52595)))
        new_user['name'] = input('Имя пользователя:')
        new_user['lastname'] = input('Фамилия пользователя:')
        new_user['age'] = input('Возраст:')
        new_user['city'] = input('Город:')
        self.my_list.append(dict(new_user))
        self.get_users()

    def change_user(self):
        new_item_search = ''
        new_item = int(input('Выберите значение какого поля мы будем менять'
                             '(цифра от 1 до 5): 1-ID, 2-Имя, 3-Фамилия,'
                             ' 4-Возраст, 5-Город... '))
        if new_item == 1:
            new_item_search = 'user_id'
        elif new_item == 2:
            new_item_search = 'name'
        elif new_item == 3:
            new_item_search = 'lastname'
        elif new_item == 4:
            new_item_search = 'age'
        elif new_item == 5:
            new_item_search = 'city'
        else:
            print('Неверный выбор')
        search_value = input(f'Введите искомое значение для'
                             f' выбранного поля {new_item_search}... ')
        for i in range(len(self.my_list)):
            self.user_item = self.my_list[i]
            for key, value in self.user_item.items():
                if value == search_value:
                    print('По условию найдена запись:\n', self.user_item)
                    if input('Вносим изменения в данные этого пользователя?'
                             ' y / n') == 'y':
                        new_value = input('Введите новое значение')
                        self.user_item[key] = new_value
                        print('Новое значение записи:', self.user_item)
                    else:
                        print('Оставляем запись без изменения')

    def del_user(self):
        new_item_search = ''
        new_item = int(input('Выберите по какому полю ищем пользователя'
                             '(цифра от 1 до 5): 1-ID, 2-Имя, 3-Фамилия,'
                             ' 4-Возраст, 5-Город... '))
        if new_item == 1:
            new_item_search = 'user_id'
        elif new_item == 2:
            new_item_search = 'name'
        elif new_item == 3:
            new_item_search = 'lastname'
        elif new_item == 4:
            new_item_search = 'age'
        elif new_item == 5:
            new_item_search = 'city'
        else:
            print('Неверный выбор')
        search_value = input(f'Введите искомое значение для'
                             f' выбранного поля {new_item_search}... ')
        for i in range(len(self.my_list)):
            self.user_item = self.my_list[i]
            for key, value in self.user_item.items():
                if value == search_value:
                    print('По условию найдена запись:\n', self.user_item)
                    if input('Удаляем данного пользователя ? y / n') == 'y':
                        # users_list = users_list.remove(user_item)
                        del self.my_list[i]
                        print('New users list:', self.my_list)
                    else:
                        print('Оставляем запись без изменения')

    def search_user(self):
        new_item_search = ''
        new_item = int(input('Выберите по какому полю ищем пользователя'
                             '(цифра от 1 до 5): 1-ID, 2-Имя, 3-Фамилия,'
                             ' 4-Возраст, 5-Город... '))
        if new_item == 1:
            new_item_search = 'user_id'
        elif new_item == 2:
            new_item_search = 'name'
        elif new_item == 3:
            new_item_search = 'lastname'
        elif new_item == 4:
            new_item_search = 'age'
        elif new_item == 5:
            new_item_search = 'city'
        else:
            print('Неверный выбор')
        search_value = input(f'Введите искомое значение для'
                             f' выбранного поля {new_item_search}... ')
        for i in range(len(self.my_list)):
            user_item = self.my_list[i]
            for key, value in user_item.items():
                if value == search_value:
                    print('По условию найдена запись:\n', user_item)

    def write_to_xlsx(self):
        headers_list = ["user_id", "name", "lastname", "age", "city"]
        wb = Workbook("users.xlsx")
        ws = wb.add_worksheet("users database")

        first_row = 0
        for header in headers_list:
            col = headers_list.index(header)
            ws.write(first_row, col, header)

        row = 1
        for dicts in self.my_list:
            for key, value in dicts.items():
                col = headers_list.index(key)
                ws.write(row, col, value)
            row += 1
        wb.close()
