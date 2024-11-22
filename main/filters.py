import django_filters
from .models import HotelRoom

class HotelRoomFilter(django_filters.FilterSet):
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = HotelRoom
        fields = ("category", "price__gte", "price__lte")

