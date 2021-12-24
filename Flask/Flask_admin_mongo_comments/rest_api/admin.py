from flask_admin.contrib.mongoengine import ModelView
from flask_admin.contrib.mongoengine.filters import FilterLike, FilterGreater, FilterSmaller
from app import admin
from rest_api.models import CPU, Tag, Vendor



# Переопределяем модели в админке
class CpuModelView(ModelView):
    column_filters = (
        FilterLike(CPU.name, 'Модель CPU'),
        FilterGreater(CPU.price, 'цена'),
        FilterSmaller(CPU.price, 'цена'),
    )


class TagModelView(ModelView):
    column_filters = (
        FilterLike(Tag.name, 'Сферы применения'),
    )


class VendorModelView(ModelView):
    column_filters = (
        FilterLike(Vendor.name, 'name'),
    )


admin.add_view(CpuModelView(CPU))
admin.add_view(TagModelView(Tag))
admin.add_view(VendorModelView(Vendor))
