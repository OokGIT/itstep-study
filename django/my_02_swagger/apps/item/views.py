from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.item.models import Item
from apps.item.serializers import ItemSerializer


class ItemsViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
