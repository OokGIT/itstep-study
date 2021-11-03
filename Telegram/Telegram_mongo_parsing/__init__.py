import telebot
import pymongo
from datetime import datetime
import conf
import wiki_search

bot = telebot.TeleBot(conf.BOT_API, parse_mode=None)
client = pymongo.MongoClient('localhost', 27017)
db = client['search_bot']


# def check_and_add_user(message):
#     if db.users.find_one({'user_id': message.from_user.id}) is None:
#         new_user = {
#             'first_name': message.from_user.first_name,
#             'last_name': message.from_user.last_name,
#             'user_id': message.from_user.id,
#             'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#             'state': 'старт'
#         }
#         db.users.insert_one(new_user)
#     return


def store_message_in_db(message):
    store_message = {
            'user_id': message.from_user.id,
            'message_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user_message': message.text,
            'state': None
        }
    db.messages.insert_one(store_message)
    return None


def get_current_state(user_id):
    user = db.users.find_one({'user_id': user_id})
    return user['state']


def set_state(user_id, state_value):
    db.users.update_one({'user_id': user_id}, {"$set": {'state': state_value}})


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
     bot.reply_to(message, "Просто введите строку и я найду для вас информацию на Википедии")


# @bot.message_handler(commands=['info'])
# def send_welcome(message):
#     u_id = message.from_user.id
#     u_name = message.from_user.first_name
#     u_lastname = message.from_user.last_name
#     u_username = message.from_user.username
#     print(u_id, u_name, u_lastname, u_username)
#     bot.reply_to(message, f"Welcome, user{u_id}, {u_name}, {u_lastname}, {u_username}")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    log_file = open(conf.LOG_FILE, 'a+', encoding="UTF-8")
    log_string = f'{datetime.now()}, - Запрос от пользователя {message.from_user.id}  {message.text} Записан в БД \n'
    log_file.write(log_string)
    log_file.close()

    # search_message_in_db(message)
    # bot.reply_to(message, f'{store_message_in_db(message)}')


bot.infinity_polling()
