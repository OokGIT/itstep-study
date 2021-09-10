class MyDict(dict):

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, my_value):
        self[key] = my_value


smarty = MyDict()
smarty.key1 = "value1"
smarty.key2 = "value2"
smarty.key3 = "value3"
smarty.key4 = "value4"

print('-------------Only values:')
for k, v in smarty.items():
    print(v)
print('-------------Pairs of key, value')
for value in smarty.items():
    print(value)
print('-------------Whole dict')
print(smarty)
