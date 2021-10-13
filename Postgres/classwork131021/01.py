import psycopg2

conn = psycopg2.connect(dbname='test01', user='postgres',
                        password='postgres', host='localhost')
cursor = conn.cursor()

cursor.execute('SELECT * FROM user_list LIMIT 10')
records = cursor.fetchall()
print(records)
for row in records:
    print(row[2])
