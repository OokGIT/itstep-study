import datetime
import requests
from bs4 import BeautifulSoup
import threading
from queue import Queue

time_start = datetime.datetime.now()

q = Queue()


def get_content(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = soup.find('title').text
    print(stories)
    q.put(stories)


urls = ['https://itc.ua', 'https://bash.im/', 'https://finance.ua', 'https://feeria.ua',
        'https://alf.ua/', 'https://www.tpg.ua/', 'https://orbita.ua/', 'https://www.flyuia.com/ua/ua/home']

threads_array = []
for u in urls:
    t = threading.Thread(target=get_content, args=(u, ))
    threads_array.append(t)

for t in threads_array:
    t.start()

for t in threads_array:
    t.join()

time_finish = datetime.datetime.now()
total_time = time_finish - time_start
print('--- Затрачено времени с потоками', total_time, ' ---\n')

time_start = datetime.datetime.now()
for u in urls:
    get_content(u)
time_finish = datetime.datetime.now()
total_time = time_finish - time_start
print('--- Затрачено времени без потоков', total_time, ' ---\n')
