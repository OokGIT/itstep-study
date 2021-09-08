# from classes import GetDictAndMakeFileName, OpenAndSerialize
# from classes import OpenAndSerialize
import json


class OpenAndSerialize:

    def __str__(self):
        # print("str input file:", input_file)
        return input_file

    def serialize(self, value):
        if type(value) == str:
            value = eval(value)
        elif type(value) == dict:
            value = str(value)
        # print("Serialized Data:", value)
        return value

    def read_file(self):
        with open(str(self)) as f:
            data = f.read()
        print("Taken date:", self.serialize(value=open(str(self), 'r').read()))
        # print("str.self-------", str(self))
        js = data
        print("New Data", js, "... With type:", type(js))

    def write_file(self):
        value = self.serialize(value=open(str(self), 'r').read())
        print("Data to be written:", value)
        file_object = open(output_file, 'w')
        # print("Запишем в новый файл:", output_file)
        file_object.write(str(value))
        file_object.close()


class ExtraSerializeGetName(OpenAndSerialize):

    def __str__(self):
        # print("str input file 22222:", output_file)
        return output_file

    def serialize(self, value):
        if type(value) == str:
            value = eval(value)
        elif type(value) == dict:
            value = str(value)
        app_json = json.dumps(value)
        # print("Serialized Data 2:", app_json)
        return app_json


# Задаём имя файла для чтения.
# В зависимости от наличия в имени text/dict выбираем что на входе.
input_file = 'input_text.txt'
output_file = 'output.json'

obj_1 = OpenAndSerialize()
obj_1.read_file()
obj_1.write_file()
print('-----------------------------------------------------')
obj_2 = ExtraSerializeGetName()
obj_2.read_file()
obj_2.write_file()
