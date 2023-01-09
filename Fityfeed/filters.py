import django_filters
from .models import *


class food_item_Filter(django_filters.FilterSet):
    class Meta:
        model = Fooditem
        fields = ['name']
