import csv
import mpu
import telebot
from geopy.point import *
import config

bot = telebot.TeleBot(config.API_KEY, parse_mode=None)

# lat1 = 50.44029
# lon1 = 30.55950
min_geo_range = 30
max_geo_range = 50


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Для получения расстояний до ближайших населенных пунктов отправьте ваши географические координаты")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    coordinates = message.text
    reg_geo = Point(coordinates).format_decimal().replace(' ', '')
    result = [float(val) for val in reg_geo.split(',')]
    lat1 = (result[0])
    lon1 = (result[1])
    rows = {}
    file = open('ua-list.csv', 'r', encoding='windows-1251')
    csv_reader = list(csv.reader(file, delimiter=';'))
    for elem in csv_reader:
        distance = mpu.haversine_distance((lat1, lon1), (float(elem[4]), float(elem[3])))
        rows[elem[2]] = distance
    file.close()
    sorted_rows = dict(sorted(rows.items(), key=lambda x: x[1]))
    final_dict = {}
    for k, v in sorted_rows.items():
        if min_geo_range <= v <= max_geo_range:
            final_dict[k] = round(v, 1)
    final_string = ("\n".join("{!r} - {!r}".format(k, v)
                              for k, v in final_dict.items())).replace("'", "").replace('"', '')
    bot.reply_to(message, final_string)


bot.infinity_polling(skip_pending=True)  # Skip pending skips old updates
