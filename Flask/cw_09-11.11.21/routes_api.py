from flask import request
from flask.json import jsonify
from jinja2 import Markup
from app import app


@app.route("/")
def hello_world():
    res_str = "Hello, World!"
    data = request.args
    key = data.get('key')

    if key:
        res_str += key

    return Markup(
        f'<div><h1>lalalala</h1><p>{res_str}</p><button>button</button></div>'
    )


@app.route("/json")
def json_route():
    # time.sleep(4)
    print(request.headers)
    return jsonify({'name': 'name', 'processor': 'intel'})


@app.route("/template")
def template_route():
    print(request)
    data = request.args


app.run(port=8048, debug=False, host='0.0.0.0')