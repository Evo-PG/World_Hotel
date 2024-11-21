from django.contrib.auth import get_user_model
from django.db import models

from main.models import HotelRoom
from payment_system.choices import PaymentApplicationStatysEnum

User = get_user_model()

class PaymentMethod(models.Model):
    title = models.CharField(max_length=35)
    logo = models.ImageField(upload_to="media/payment_method_logo") # Логотип банка
    qr = models.ImageField(upload_to="media/payment_method_qr")
    person_account = models.CharField(max_length=30) # лицевой счот

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'

class HotelPaymentApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=40) # название способа оплаты
    payment_check = models.FileField(upload_to="media/payment_check")
    status = models.CharField(max_length=100,
        choices=PaymentApplicationStatysEnum.choices,
        default=PaymentApplicationStatysEnum.IN_PROGRESS,
    )
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на оплату Номера'
        verbose_name_plural = 'Заявки на оплату Намеров'

