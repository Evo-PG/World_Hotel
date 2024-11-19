from django.shortcuts import render, redirect, get_object_or_404

from user.forms import MyUserRegisterForms
from .models import HotelRoom, Services, Category,HotelRoomImage


def index_viu(request):

    register_form = MyUserRegisterForms()
    hotel_rooms = HotelRoom.objects.all()
    services = Services.objects.all()

    return render(
        request=request,
        template_name='main/index.html',
        context={
            "hotel_rooms":hotel_rooms,
            "services":services,
            "register_form":register_form
        }
    )

def ditail_viu(request, pk):
    hotel_room_ditail = get_object_or_404(HotelRoom, id=pk)
    image_hotel_room = HotelRoomImage.objects.filter(hotel_room=hotel_room_ditail)

    return render(
        request=request,
        template_name='main/ditail.html',
        context={
            "hotel_room_ditail": hotel_room_ditail,
            "image_hotel_room": image_hotel_room,  # передаем все изображения
        }
    )

