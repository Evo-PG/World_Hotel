from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import HotelRoom
from .models import PaymentMethod, HotelPaymentApplication

# главная страница оплаты
def payment_system_veu(request, pk):
    tour = get_object_or_404(HotelRoom, id=pk)
    payment_method = PaymentMethod.objects.all()

    if request.method == "POST":
        # Проверяем, был ли прикреплён чек
        if 'check' in request.FILES:
            payment_check = request.FILES['check']  # Получаем файл чека
            method_payment = request.POST.get("method_payment")

            tour_payment_application = HotelPaymentApplication(
                tour=tour,
                user=request.user,
                payment_method=method_payment,
                payment_check=payment_check
            )

            tour_payment_application.save()
            return redirect("index")
        else:
            messages.error(request, "Вы забыли прикрепить чек")  # Используйте messages.error для ошибки

    return render(
        request=request,
        template_name="payment_system/payment_system.html",
        context={
            "payment_methods": payment_method,
            "tour": tour,
        }
    )

def my_payment_applications_veu(request):
    application = HotelPaymentApplication.objects.filter(user=request.user)

    return render(
        request=request,
        template_name="payment_system/my_payment_application.html",
        context={
            "applications":application
        }
    )


