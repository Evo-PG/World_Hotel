from django.shortcuts import render
from .models import HotelRoom, Services,Category
from django.views.generic import ListView


def index_viu(request):
    hotel_rooms = HotelRoom.objects.all()
    services = Services.objects.all()

    return render(
        request=request,
        template_name='main/index.html',
        context={
            "hotel_rooms":hotel_rooms,
            "services":services
        }
    )

def test(request):

    return render(
        request=request,
        template_name='main/test.html'
    )

