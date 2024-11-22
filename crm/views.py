from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from main.models import HotelRoom
from payment_system.choices import PaymentApplicationStatysEnum
from payment_system.models import HotelPaymentApplication
from .models import Crm

def payment_request_veu(request):

    if not request.user.is_authenticated or not request.user.is_admin and request.user.status == 2:
        return redirect("index")

    applications = HotelPaymentApplication.objects.filter(status__in=['in_progress', 'denied']).order_by("-id")

    payment_choices = PaymentApplicationStatysEnum

    paginator = Paginator(applications, 20)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request=request,
                  template_name="crm/payment_request.html",
                  context={
                      "applications":applications,
                      "payment_choices":payment_choices,
                      "page_obj":page_obj
                      }
                  )

def payment_request_update_statys_veu(request, application_id):
    application = get_object_or_404(HotelPaymentApplication, id=application_id)

    if request.method == "POST":
        if "statys" in request.POST:
            statys = request.POST["statys"]

            if statys == 'accepted':
                end_payment = Crm(
                    user=application.user.full_name,
                    hotel=application.hotel_room.number_room_hotel,
                    category=application.hotel_room.category,
                    payment_method=application.payment_method,
                    payment_check=application.payment_check,
                    status="Принято"
                )
                end_payment.save()

            application.status = statys
            application.save()
            return redirect("payment_request")

    return redirect("payment_request")


def dashboard_viu(request):
    if not request.user.is_authenticated or not request.user.is_admin and request.user.status == 2:
        return redirect("index")

    return render(request, "crm/dashbord.html")

def tour_end_payments_viu(request):
    if not request.user.is_authenticated or not request.user.is_admin and request.user.status == 2:
        return redirect("index")

    crms = Crm.objects.all()

    return render(request, "crm/tour_end_payments.html",{"crms":crms})

from django.shortcuts import render

def update_status(request, room_id):
    room = get_object_or_404(HotelRoom, id=room_id)

    if request.method == "POST":
        if "status" in request.POST:
            status = request.POST["status"]
            room.status = status
            room.save()
            return redirect("update_statys")  # Переадресация на страницу с номерами

    return redirect("update_statys")


def hotel_room_veu(request):
    # Проверка на аутентификацию пользователя и его роль
    if not request.user.is_authenticated or not request.user.is_admin and request.user.status == 2:
        return redirect("index")

    # Получаем все номера отеля
    rooms = HotelRoom.objects.all().order_by("-id")

    # Настройки пагинации
    paginator = Paginator(rooms, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request=request,
                  template_name="crm/hotel_room_list.html",  # Ваш шаблон для отображения
                  context={
                      "rooms": rooms,
                      "page_obj": page_obj
                  })

