class SmartDict:

    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        keys_self = list(self.__dict__.keys())
        values_self = list(self.__dict__.values())
        if self.index == len(keys_self):
            self.index = 0
            raise StopIteration
        return keys_self[self.index], values_self[self.index]

    def __getattr__(self, my_key):
        print("got it")
        return self.__dict__[my_key]

    def __setattr__(self, my_key, my_value):
        self.__dict__[my_key] = my_value
        # print(my_key, my_value)

    # def my_func(self):
    #     # self.__dict__.pop('index', 0)
    #     print(list(self.__dict__.keys()), list(self.__dict__.values()))
    #     print(list(self.__dict__.items()))


smarty = SmartDict()

smarty.key1 = "data1"
smarty.key2 = "data2"
smarty.key3 = "data3"
smarty.key4 = "data4"
smarty.key5 = "data5"

# smarty.my_func()
print("---------------")
# for key, value in smarty: print(value) вернёт только value, как и надо.
# Но как сделать итерацию for value только? Пока не придумалось.
for key, value in smarty:
    print(value)
print("---------------")
for key, value in smarty:
    print(key, value)
