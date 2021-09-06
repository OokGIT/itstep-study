# from classes import GetDictAndMakeFileName, OpenAndSerialize
from classes import OpenAndSerialize

# Задаём имя файла для чтения
input_file = 'input_text.txt'


obj_get = OpenAndSerialize(input_file)
# obj_get.read_file()
obj_get.serialize()
