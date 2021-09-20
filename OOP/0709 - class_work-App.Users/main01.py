class UserClass:

    def __init__(self, user_id, user_name, user_lastname='', user_age=0, user_city='Kyiv'):
        self.user_id = user_id
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_age = user_age
        self.user_city = user_city

    def add_user(self):
        return None

    def search_user(self):
        obj = next(filter(lambda obj: obj.name, list), None)
        print(obj)

    def get_info(self):
        return None

    def get_fields(self):
        return None

    def change_info(self, field_name, new_field_name):
        if getattr(self, field_name):
            setattr(self, field_name, new_field_name)


first_user = UserClass(user_id=1, user_name='Ivan')
second_user = UserClass(user_id=2, user_name='Anastasiia')

# Меню
a = int(input("Добавить 1  Найти 2"))
if a == 2:
    user = UserClass
    user.search_user(1)
list_users = []


