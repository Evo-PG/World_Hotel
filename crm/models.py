from django.db import models

class Crm(models.Model):
    user = models.CharField(max_length=80)
    hotel = models.CharField(max_length=90)
    category = models.CharField(max_length=90)
    payment_method = models.CharField(max_length=40) # название способа оплаты
    payment_check = models.FileField(upload_to="media/payment_check")
    status = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel

    class Meta:
        verbose_name = 'Принятая заявка на оплату Тура'
        verbose_name_plural = 'Принятые заявки на оплату Тура'

