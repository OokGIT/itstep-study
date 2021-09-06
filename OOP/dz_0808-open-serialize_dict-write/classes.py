class OpenAndSerialize:

    def __init__(self, file_name):
        self.file_name = file_name

    def serialize(self):
        if self.read_file() is True:
            print("serialize:", self.read_file())

    def __str__(self):
        return "output_file.one"

    def read_file(self):
        file = open(self.file_name, 'r')
        contents = file.read()
        file.close()
        # print(type(contents))
        if type(contents) == dict:
            # print(contents)
            return contents
        elif type(contents) == str:
            dictionary = eval(contents)
            # print(dictionary)
            return dictionary
        else:
            return None


