# Магические методы
# https://habr.com/ru/post/186608/

class smartDict:

    def __getattr__(self, key):
        print(key)
        print("key", key)

        return self.__dict__[key]

    def __setattr__(self, key, value):
        print('----')
        print("key", key)
        print("value", value)
        self.__dict__[key] = value

    def _func(self):
        print('_func')
        print(list(self.__dict__.keys()))




class IterClass:

    def __init__(self, value_list):
        self.index = 0
        self.value_list = value_list

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        # keys_self = list(self.__dict__.keys())
        keys_self = list(self.value_list)

        if self.index == len(keys_self):
            self.index = 0
            raise StopIteration

        return self.value_list[self.index]


# Написать универсальный класс который примимает значение через setattr
# таким образом
# smarty = smartDict()
# smarty.name1 = "value1"
# smarty.name2 = "value2"
# smarty.name3 = "value3"
#
# В результате получиться внутренный дикт {"name1":"value1", **} -> self.__dict__
#
# который сможет итерироватся через :
#
# for value in smarty:
#     print(value)
#
#
# но приетом будет печатать в консоль значение а не ключь print(value) -> value1
#
#
# * сделать так чтоб при итерации выводился еще и ключ
#
# for key, value in smarty:
#     print(key)
#     print(value)