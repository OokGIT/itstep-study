from flask import Response, request, jsonify
from app import app
from rest_api.models import User


@app.route('/user/')
def get_list_user():
    query_params = dict(request.args)
    print(query_params)
    # query page param

    users = User.objects.filter(**query_params)
    # pagination

    # create serializer or use lib after
    # return Response(users)

    return jsonify(users)


@app.route('/user/<id_user>')
def get_user_by_id(id_user):
    print('aaaaaaaaaaa')
    print(id_user)

    data = User.objects.get(id=id_user)
    # FIX IT

    # create serializer or use lib after
    # data = serializer = Serializer(user)
    # return Response(users)

    return jsonify(data)


@app.route('/user/', methods=['POST'])
def create_user():
    data = request.json
    print(data)
    # 'name_1' - fix it

    users = User.objects.create(**data)

    return Response(users, status=201)


@app.route('/user/<id_user>', methods=['DELETE'])
def delete_user_by_id(id_user):
    User.objects.get(id=id_user).delete()
    # FIX it bad id

    # create serializer or use lib after
    # return Response(users)

    return Response({'status': 'deleted'}, status=200)


@app.route('/user/<id_user>', methods=['PUT'])
def put_user_by_id(id_user):
    # For rewrite obj

    data = request.json
    user = User.objects.get(id=id_user).update(**data)

    # create serializer or use lib after
    # return Response(users)

    return Response(user, status=200)


@app.route('/user/<id_user>', methods=['PATCH'])
def patch_user_by_id(id_user):
    # For one field or some

    # FIX it bad data - request.json
    data = request.json
    user = User.objects.get(id=id_user).update(**data)

    # create serializer or use lib after
    # return Response(users)

    return Response(user, status=200)
