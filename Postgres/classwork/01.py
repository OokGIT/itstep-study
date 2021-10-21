import psycopg2

conn = psycopg2.connect(dbname='test01', user='postgres',
                        password='postgres', host='localhost')
cur = conn.cursor()

create_users = '''CREATE TABLE users
(   
    user_id   serial PRIMARY KEY,
    username "char"
);
'''

cur.execute(create_users)
conn.commit()
records = cur.fetchall()
print(records)
for row in records:
    print(row[2])
