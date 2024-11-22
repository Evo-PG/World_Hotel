from django import forms
from .models import HotelRoom, Category,Services

class HotelRoomForm(forms.ModelForm):
    class Meta:
        model = HotelRoom
        fields = ['number_bets','number_withdrawals','number_room_hotel', 'cover', 'description', 'prise', 'category', 'number_room', 'status']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', ]

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title', 'smol_description', 'description', 'cover']

