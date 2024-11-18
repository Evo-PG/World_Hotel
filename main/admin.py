from django.contrib import admin
from .models import Category, HotelRoom,Services

admin.site.register(Category)
admin.site.register(HotelRoom)
admin.site.register(Services)
