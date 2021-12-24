from flask import render_template
from rest_api.models import CPU
from app import app


@app.route('/')
def index_page():
    res = CPU.objects()
    # res = [
    #     {'name': 'Intel Core i5-10400', 'freq': '2.9GHz', 'cache': '12MB', 'price': '5359'},
    #     {'name': 'Intel Core i7-11700K', 'freq': '3.6Hz', 'cache': '16MB', 'price': '12011'},
    #     {'name': 'Intel Core i5-10400F', 'freq': '2.9GHz', 'cache': '12MB', 'price': '4799'},
    #     {'name': 'Intel Core i9-12900K', 'freq': '3.2GHz', 'cache': '30MB', 'price': '21299'},
    #     {'name': 'AMD Ryzen 5 5600X', 'freq': '3.7GHz', 'cache': '32MB', 'price': '9365'},
    # ]
    print(res)
    return render_template('index.html', name='Процессоры', result=res)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/comments')
def comments():
    return render_template('comments.html')


@app.route('/item')
def item():
    return render_template('item.html')
