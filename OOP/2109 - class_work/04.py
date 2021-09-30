# вход текст, выход два слова - наиболее встречающееся и самое длинное
my_string = 'Основным отличием Компьютерной Академии "ШАГ" от других учебных ' \
            'заведений IT-профиля является четкая ориентация на современные ' \
            'технологии, мощная техническая и методическая база, современное ' \
            'компьютерное оборудование и профессиональные преподаватели - ' \
            'практики. '

count = 0
word = ''
maxCount = 0
max_word = ''
words = []
my_list = my_string.split()
# print(my_list)

for i in range(0, len(my_list)):
    count = 1
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            count += count
        if len(my_list[i]) > len(max_word):
            max_word = my_list[i]
    if count > maxCount:
        maxCount = count
        word = my_list[i]

print('Самое частое слово:', word)
print('Самое длинное слово:', max_word)
