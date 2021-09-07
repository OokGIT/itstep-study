# import json

class OpenAndSerialize:

    def __init__(self, file_name):
        self.file_name = file_name

    def serialize(self, value):
        if type(self.value) == dict:
            self.value = str(self.value)
            return value
        elif type(self.value) == str:
            self.value = eval(self.value)
            return value

    def read_file(self, file_name):
        file = open(self.file_name, 'r')
        contents = self.serialize(file_name)
        return contents
        file.close()
