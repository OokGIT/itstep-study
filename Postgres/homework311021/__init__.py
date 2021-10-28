# https://dev-gang.ru/article/rabota-s-postgresql-v-python-xn8721sq0g/
#
# Создать таблицы с помощью python через psycopg2
#
#
# Наполнить бд через комманду insert into
import models

# # Создадим таблицы
# models.cursor.execute(models.create_table_posts)
# models.cursor.execute(models.create_table_users)
# models.cursor.execute(models.create_table_m2m)
# models.con.commit()

# Наполним БД
# # users
# models.insert_users('mark', 24)
# models.insert_users('ivan', 12)
# models.insert_users('eva', 28)
# models.insert_users('justin', 45)
# # posts
# models.insert_posts('hello world!', '10.12.2021')
# models.insert_posts('im here', '01.05.2020')
# models.insert_posts('price needed', '08.08.2008')
# models.insert_posts('best course ever!!', '24.06.2020')
# # m2m - залинковали соответствующие посты с пользователями
# models.assign_u2p(1, 1, 8)
# con.commit()
# cursor.execute(f'''INSERT INTO users (username, age) VALUES ('mark', '24')''')
# con.commit()

# Testing (тут проверили, что при удалении поста удаляется запись в таблице many-to-many:
del_post = 1
del_query = f'''DELETE FROM posts WHERE post_id = {del_post}'''
models.cursor.execute(del_query)
models.con.commit()
