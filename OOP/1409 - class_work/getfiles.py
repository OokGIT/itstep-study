import os
my_directory = './'
my_parentdir = '../'
files = os.listdir(my_directory)
upper_files = os.listdir(my_parentdir)
print('Содержимое рабочего каталога:\n', files)
print('Содержимое родительского каталога:\n', upper_files)