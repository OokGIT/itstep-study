import telebot
import config

bot = telebot.TeleBot(config.BOT_API, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['info'])
def send_welcome(message):
    u_id = message.from_user.id
    u_name = message.from_user.first_name
    u_lastname = message.from_user.last_name
    u_username = message.from_user.username
    print(u_id, u_name, u_lastname, u_username)
    bot.reply_to(message, f"Welcome, user{u_id}, {u_name}, {u_lastname}, {u_username}")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.text)
    print(message.from_user.id)
    bot.reply_to(message, 'message, message.text')


bot.infinity_polling()
