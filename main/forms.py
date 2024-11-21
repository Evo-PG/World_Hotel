from django import forms
from .models import HotelRoom

class HotelRoomForms(forms.ModelForm):
    class Meta:
        model = HotelRoom
        fields = ["number_room_hotel", "number_bets", "number_withdrawals", "cover", "description", "prise", "category", "number_room"]
        widgets = {
            'number_room_hotel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер комнаты'}),
            'number_bets': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество кроватей'}),
            'number_withdrawals': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество выходов'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Описание'}),
            'prise': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'number_room': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество номеров'}),
        }
