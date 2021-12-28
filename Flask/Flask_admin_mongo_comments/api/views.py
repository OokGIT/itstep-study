import mongoengine.base.datastructures
from flask import render_template, Response, request, jsonify, send_from_directory
from mongoengine.base import BaseList
from rest_api.models import CPU, Vendor, Comment
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
    # print(res)
    return render_template('index.html', name='Процессоры', result=res)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/comments')
def comments():
    return render_template('comments.html')


class BadParams(Exception):
    pass


MAP_ENDPOINT_MODELS = {
    "/item": CPU,
    "/vendor": Vendor,
}

INCONTAINS_FILTER_FIELDS = ["name"]

def _check_query():
    query_params = dict(request.args)
    model = MAP_ENDPOINT_MODELS[request.path]
    models_keys = set(model._db_field_map.keys())
    query_keys = set([*query_params.keys(), 'id'])
    diff_keys = query_keys - models_keys
    # print(diff_keys)
    if diff_keys:
        raise BadParams(f"{diff_keys}")


def decorator_check(func):
    def _wrap_(*args, **kwargs):

        try:
            _check_query()
        except BadParams as e:
            return Response(f"Error in parameter {e}", 400)
        return func(*args, **kwargs)
    _wrap_.__name__ = func.__name__
    return _wrap_


def _change_params(query_params: dict) -> dict:
    filter_params = {}
    for key in query_params.keys():
        if key in INCONTAINS_FILTER_FIELDS:
            filter_params[f"{key}__icontains"] = query_params[key]
    return filter_params


def serializer(models_objs):
    list_data = []
    for obj in models_objs:
        keys = obj._db_field_map.keys()
        _obj = {}
        for key in keys:
            value = getattr(obj, key)
            if type(value) == BaseList:
                value = serializer(value)
            else:
                value = str(value).rstrip()
            _obj[key] = value
        list_data.append(_obj)
    return list_data


# @app.route('/item_id')
# def


@app.route('/item/<item_id>')
def get_item_by_id(item_id):
    print(item_id)
    item = CPU.objects.get(id=item_id)
    print(item.name)
    return render_template('item.html', item=item)


@app.route('/item/img/<file>')
def static_file_img(file):
    return send_from_directory('templates/img/', file)


@app.route('/item')
@decorator_check
def view_get_item():
    query_params = dict(request.args)
    filter_query = _change_params(query_params=query_params)
    # print(query_params)
    items = CPU.objects.filter(**filter_query)
    data = serializer(items)
    json_out = jsonify(data)
    return render_template('item.html', name='Процессор', result=data)


@app.route('/vendor')
@decorator_check
def view_get_vendor():
    query_params = dict(request.args)
    filter_query = _change_params(query_params=query_params)
    # print(query_params)
    vendor = Vendor.objects.filter(**filter_query)
    data = serializer(vendor)
    return jsonify(data), 200


@app.route('/get_comments/<id_item>')
def get_comments(id_item):
    comment = Comment.objects.filter(item=id_item)
    data = serializer(comment)
    return jsonify(data), 200


@app.route('/send_comment/<id_item>', methods=['POST'])
def save_comments(id_item):
    data_to_save = request.json
    data_to_save['item'] = id_item
    comment = Comment(**data_to_save)
    comment.save()
    return jsonify({}), 200
