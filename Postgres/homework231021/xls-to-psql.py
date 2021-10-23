import psycopg2
import config
conn = psycopg2.connect(dbname=config.dbname, user=config.dbuser,
                        password=config.dbpass, host=config.dbhost)
cursor = conn.cursor()


create_table_query_news = '''CREATE TABLE news
(ID SERIAL PRIMARY KEY,
NEWS_HEADER TEXT,
NEWS_TEST TEXT,
NEWS_PUBLISH_DATE DATE,
NEWS_LINK TEXT);'''

create_table_query_media = '''CREATE TABLE media
(ID SERIAL PRIMARY KEY,
MEDIA_TYPE TEXT,
MEDIA_SOURCE TEXT,
MEDIA_RATE TEXT,
MEDIA_HEADING TEXT,
MEDIA_CIRCULATION TEXT);'''

create_table_query_geo = '''CREATE TABLE geo
(ID SERIAL PRIMARY KEY,
GEO_COUNTRY TEXT,
GEO_REGION TEXT,
GEO_CITY TEXT,
GEO_LINK TEXT);'''

cursor.execute(create_table_query_news)
cursor.execute(create_table_query_media)
cursor.execute(create_table_query_geo)
conn.commit()
