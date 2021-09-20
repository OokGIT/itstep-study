import csv
users_list = [{'user_id': 18456, 'name': 'Артем', 'lastname': 'Данилов',
               'age': 40, 'city': 'Херсон'}, {'user_id': 40385, 'name': 'Иван',
                                              'lastname': 'Гончаренко',
                                              'age': 44, 'city': 'Ереван'}]


class User_Db:

    # def __init__(self):
    #     self.user_list = []

    def save_cvs(self, *args):
        keys = my_dict[0].keys()
        with open('users_list.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(users_list)
        print(users_list)

my_dict = User_Db(users_list)
my_dict.save_cvs()
