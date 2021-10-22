import project_func

# project_func.get_db_info()
#
# Создаем таблицы, на вход функции отправляем имя таблицы. Поля предопределены заранее
# project_func.create_table('phones06')
# project_func.create_table('phones08')

# Заполняем таблицу данными
# project_func.fill_data('phones08', 'Mi9', 8650)

# Запишем в БД новую цену
# project_func.update_price('phones08', 2, 555555)

# Найдем телефоны дешевле указанной цены
project_func.search_min_price('phones08', 9000)
