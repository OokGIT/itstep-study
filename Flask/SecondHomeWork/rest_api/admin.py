from flask_admin.contrib.mongoengine import ModelView
from flask_admin.contrib.mongoengine.filters import FilterEqual, FilterLike
from rest_api.models import User
from app import admin


class UserModelView(ModelView):
    column_filters = (
        FilterLike(User.name, 'name'),
        FilterEqual(User.last_name, 'last_name'),
    )


admin.add_view(UserModelView(User))
