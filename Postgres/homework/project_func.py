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
(ID INT PRIMARY KEY NOT NULL,
MODEL   TEXT    NOT NULL,
PRICE   REAL);'''
    cursor.execute(create_table_query)
    conn.commit()
    print("Создана таблица", tb_name)


def fill_data(table_name, mobile_id, mobile_model, mobile_price):
    insert_query = f''' INSERT INTO {table_name} (ID, MODEL, PRICE) VALUES ({mobile_id}, '{mobile_model}', {mobile_price})'''
    # insert_query = ''' INSERT INTO phones07 (ID, MODEL, PRICE) VALUES (1, 'huaweii', 10000)'''
    cursor.execute(insert_query)
    conn.commit()
    print("Запись создана")
    cursor.execute(f"SELECT * from {table_name}")
    record = cursor.fetchall()
    print("Результат:", record)
