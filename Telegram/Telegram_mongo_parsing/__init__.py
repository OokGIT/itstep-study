import telebot
import conf
import functions
from datetime import datetime

bot = telebot.TeleBot(conf.BOT_API, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Напишите что-то и я поищу это для вас"
                          " на Википедии")


@bot.message_handler(func=lambda m: True)
def catch_all(message):
    log_file = open(conf.LOG_FILE, 'a+', encoding="UTF-8")
    log_string = f'{datetime.now()}, - Запрос от пользователя' \
                 f' {message.from_user.first_name} "{message.text}" Записан в БД \n'
    log_file.write(log_string)
    log_file.close()
    functions.store_message_to_db(message)
    bot.send_message(message.chat.id, functions.db_update(message.text))
    # bot.send_message(message.chat.id, functions.search_in_db(message.text, message.chat.id))
    print(message.text)

    # bot.reply_to(message, f'{store_message_to_db(message)}')

# while True:
#     functions.db_filter()

bot.infinity_polling()
