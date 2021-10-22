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
    print("Создана таблица")


