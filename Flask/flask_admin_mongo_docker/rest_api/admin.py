from flask_admin.contrib.mongoengine import ModelView
from flask_admin.contrib.mongoengine.filters import FilterLike, FilterGreater, FilterSmaller
from models import CPU
from ..app import admin


# Переопределяем модели в админке
class UserModelView(ModelView):
    column_filters = (
        FilterLike(CPU.name, 'наименование'),
        FilterGreater(CPU.price, 'цена'),
        FilterSmaller(CPU.price, 'цена'),
    )


admin.add_view(UserModelView(CPU))
