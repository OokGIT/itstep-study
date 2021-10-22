import psycopg2
import config
conn = psycopg2.connect(user=config.dbuser,
                        password=config.dbpass,
                        host=config.dbhost,
                        database=config.dbname)
cursor = conn.cursor()


def get_db_info():
    cursor.execute("SELECT version();")
    print("Версия БД:", cursor.fetchone())
    print("Схема подключения:", conn.get_dsn_parameters())


def create_table(tb_name):
    create_table_query = f'''CREATE TABLE {tb_name}
(ID SERIAL PRIMARY KEY,
MODEL   TEXT    NOT NULL,
PRICE   REAL);'''
    cursor.execute(create_table_query)
    conn.commit()
    print("Создана таблица", tb_name)


def fill_data(table_name, mobile_model, mobile_price):
    insert_query = f''' INSERT INTO {table_name} (MODEL, PRICE) VALUES ('{mobile_model}', {mobile_price})'''
    cursor.execute(insert_query)
    conn.commit()
    print("Запись создана")
    cursor.execute(f"SELECT * from {table_name}")
    record = cursor.fetchall()
    print("Результат:", record)


def update_price(table_name, mobile_id, new_price):
    update_query = f'''UPDATE {table_name} SET PRICE = {new_price} WHERE ID = {mobile_id}'''
    cursor.execute(update_query)
    conn.commit()
    print("Цена обновлена")
    cursor.execute(f"SELECT * from {table_name}")
    record = cursor.fetchall()
    print("Результат:", record)


def search_min_price(table_name, search_price):
    search_query = f''' SELECT * FROM {table_name} WHERE PRICE < {search_price}'''
    cursor.execute(search_query)
    record = cursor.fetchall()
    print(record)
