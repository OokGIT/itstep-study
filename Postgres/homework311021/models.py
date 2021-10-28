import psycopg2
import config

con = psycopg2.connect(
    database=config.dbname,
    user=config.dbuser,
    password=config.dbpass,
    host=config.dbhost
)

cursor = con.cursor()

# --------------------------------------
# Тут просто создадим таблицы
create_table_users = '''CREATE TABLE users (
    user_id serial PRIMARY KEY,
    username text NOT NULL,
    age numeric NOT NULL DEFAULT 0
);'''

create_table_posts = '''CREATE TABLE posts (
    post_id serial PRIMARY KEY,
    title text NOT NULL,
    date date NOT NULL DEFAULT CURRENT_DATE
);'''

create_table_m2m = '''CREATE TABLE many_to_many_up (
    post_id int REFERENCES posts (post_id) ON UPDATE CASCADE ON DELETE CASCADE,
    user_id int REFERENCES users (user_id) ON UPDATE CASCADE,
    amount numeric NOT NULL DEFAULT 1,
    CONSTRAINT user_post_keys PRIMARY KEY (post_id, user_id)
);'''
# --------------------------------------


# Функции наполнения таблиц данными и линковки m2m
def insert_users(get_user, get_age):
    insert_query = f'''INSERT INTO users (username, age) VALUES ('{get_user}', '{get_age}')'''
    cursor.execute(insert_query)
    con.commit()


def insert_posts(get_title, get_date):
    insert_query = f'''INSERT INTO posts (title, date) VALUES ('{get_title}', '{get_date}')'''
    cursor.execute(insert_query)
    con.commit()


def assign_u2p(get_uid, get_pid, get_amount):
    insert_query = f'''INSERT INTO many_to_many_up (post_id, user_id, amount)
     VALUES ('{get_uid}', '{get_pid}', {get_amount})'''
    cursor.execute(insert_query)
    con.commit()
