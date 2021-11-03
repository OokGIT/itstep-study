import wikipedia
import pymongo
from datetime import datetime
import conf

client = pymongo.MongoClient(conf.DB_HOSTNAME, conf.DB_PORT)
db = client[conf.DB_NAME]
wikipedia.set_lang(conf.WIKI_LANGUAGE)


# запрос через модуль wikipedia заголовка статьи по отправленному пользователем тексту
def wiki_search_summary(message):
    result = wikipedia.summary(f'{message}')
    # print(result)
    return result


# все запросы пользователя сразу кладём в бд и помечаем, что по ним ещё нет ответа wiki (state: None)
def store_message_to_db(message):
    store_message = {
          'user_id': message.from_user.id,
          'message_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
          'user_message': message.text,
          'response': "",
          'state': None
          }
    db.messages.insert_one(store_message)
    return None


def db_update(message):
    response = None
    for doc in db.messages.find():
        # print(doc)
        # db.messages.update_many({"state": None}, {'$set': {"state": True}})
        if doc['state'] is None and doc['user_message'] == message:
            response = wiki_search_summary(message)
            # print(response)
            # user = doc['user_id']
            # print(user)
            db.messages.update_one({'_id': doc['_id']}, {'$set': {"state": True}})
            db.messages.update_one({'_id': doc['_id']}, {'$set': {"response": response}})
        elif doc['state'] is True and doc['user_message'] == message:
            response = doc['response']
    return response


# def search_in_db(message, user_id):
#     response = None
#     print(message)
#     print(user_id)
#     for doc in db.messages.find():
#         if doc['user_message'] == message and doc['user_id'] == user_id and doc['state'] is True:
#             response = doc['response']
#     print(response)
#     return response
