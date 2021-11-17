import time

import requests
from flask import Flask, request, render_template\
    # , url_for
from flask.json import jsonify
from jinja2 import Markup

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', name='Процессоры')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:u_id>')
def user(name, u_id):
    return 'User page: ' + name + '-' + str(u_id)


@app.route('/user/')
def user_by_key():
    res_str = "Hello, your's credentials is: "
    data = request.args
    u_name = data.get('u_name')
    u_id = data.get('u_id')

    if u_name:
        res_str += u_name
    if u_id:
        res_str += u_id
    return Markup(f"<div><p>{res_str}</p><button>button_1</button><iframe src='/json'/></div>")


@app.route('/json')
def json_route():
    time.sleep(2)
    # print(request.headers)
    return jsonify({'vendor': 'Intel', 'model': 'Xeon 5940 v.3'})
