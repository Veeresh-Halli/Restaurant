import django_filters
from django_filters import NumberFilter
from .models import Menu

class MenuItem(django_filters.FilterSet):
    price = NumberFilter(field_name='price', lookup_expr="lte")
    class Meta:
        model = Menu
        fields = ['category', 'food_type']