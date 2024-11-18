from django.shortcuts import render
from .models import HotelRoom, Services,Category
from django.views.generic import ListView


def index_viu(request):
    hotel_room = HotelRoom.objects.all().exclude(status=1).order_by('-id')[:3]
    services = Services.objects.all()

    return render(
        request=request,
        template_name='main/index.html',
        context={
            "hotel_room":hotel_room,
            "services":services
        }
    )

def test(request):

    return render(
        request=request,
        template_name='main/test.html'
    )

