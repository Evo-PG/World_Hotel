from django.contrib import admin
from .models import Category, HotelRoom,Services, HotelRoomImage

admin.site.register(Category)
admin.site.register(HotelRoom)
admin.site.register(HotelRoomImage)
admin.site.register(Services)
