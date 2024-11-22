from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from user.forms import MyUserRegisterForms
from .filters import HotelRoomFilter
from .models import HotelRoom, Services, Category
from .forms import HotelRoomForm, CategoryForm, ServicesForm


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

    return render(
        request=request,
        template_name='main/ditail.html',
        context={
            "hotel_room_ditail": hotel_room_ditail,
        }
    )


def add_hotel_room(request):
    form = HotelRoomForm()

    if request.method == "POST":
        form = HotelRoomForm(request.POST, request.FILES)  # не забывай про файлы
        if form.is_valid():
            form.save()
            return redirect("create_hotel_room")

    return render(request, 'main/add_hotel_room.html', {"form": form})

def add_category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_category")

    return render(request, 'main/add_categiry.html', {"form": form})

def add_services(request):
    form = ServicesForm()

    if request.method == "POST":
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("create_category")

    return render(request, 'main/add_serves.html', {"form": form})

def event_list_viu(request):
    hotel_room = HotelRoomFilter(request.GET, queryset=HotelRoom.objects.filter(status=1))

    categories = Category.objects.all()

    paginator = Paginator(hotel_room.qs, 9)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request=request,
        template_name='main/event_list.html',
        context={
            'tours': hotel_room,
            'page_obj': page_obj,
            'categories': categories
        }
    )
