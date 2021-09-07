# from classes import GetDictAndMakeFileName, OpenAndSerialize
# from classes import OpenAndSerialize
import json


class OpenAndSerialize:

    def __init__(self, file_name):
        self.file_name = file_name
        print("Приняли имя файла:", self.file_name)

    def __str__(self):
        return input_file

    def serialize(self, value):
        print("Сериализатор 1, вход:", value)
        # value = eval(value)
        print("Сериализатор 1, выход:", value)
        return value

    def read_file(self):
        file_json = json.loads(self.serialize(open(str(self), 'r').read()))
        # contents = self.serialize(file_name)
        print("Из файла", self, "забираем такой json:", file_json)
        return file_json
        file.close()

    def write_file(self):
        value = self.serialize(self)
        file = open(str(self), 'w')
        print("Запишем в новый файл:", output_file)
        file.write(str(value))
        file.close()
        return value


class ExtraSerializeGetName(OpenAndSerialize):

    def __str__(self):
        # value = super().__str__()
        return output_file

    def serialize(self, value):
        if type(value) == str:
            value = eval(value)
        if type(value) == dict:
            value = str(value)
        print("Сериализатор2:", value)
        return value


# Задаём имя файла для чтения
input_file = 'input_text.txt'
output_file = 'output.json'

# obj_get = ExtraSerializeGetName(input_file)
# obj_get.read_file()

obj_1 = OpenAndSerialize(input_file)
obj_1.read_file()

obj_2 = ExtraSerializeGetName(output_file)
obj_2.write_file()

# obj_2.write_file(output_file)
